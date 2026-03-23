"""
Community Health Tracker
========================
Tracks and visualises key health metrics for an open source community.
Metrics: new members, active contributors, issues opened/closed, events held.

Author: Owolabi Samuel Ogunlalu
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

# ── Sample Data ──────────────────────────────────────────────────────────────
# In a real deployment this would load from a CSV export or API (e.g. GitHub API,
# Discourse API, Zulip). Here we use realistic synthetic data for demonstration.

data = {
    "month": [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ],
    "new_members":        [12, 18, 15, 22, 30, 28, 35, 40, 38, 45, 50, 60],
    "active_contributors":[5,  8,  7,  10, 14, 13, 16, 20, 19, 23, 27, 32],
    "issues_opened":      [8,  12, 10, 15, 20, 18, 22, 25, 23, 28, 30, 35],
    "issues_closed":      [6,  10, 9,  13, 17, 16, 20, 22, 21, 25, 28, 33],
    "events_held":        [1,  1,  2,  2,  3,  2,  3,  4,  3,  4,  4,  5],
}

df = pd.DataFrame(data)


# ── Derived Metrics ───────────────────────────────────────────────────────────

df["issue_resolution_rate"] = (df["issues_closed"] / df["issues_opened"] * 100).round(1)
df["contributor_ratio"]     = (df["active_contributors"] / df["new_members"] * 100).round(1)
cumulative_members          = df["new_members"].cumsum()


# ── Summary Statistics ────────────────────────────────────────────────────────

def print_summary(df):
    print("=" * 52)
    print("   COMMUNITY HEALTH REPORT — FULL YEAR SUMMARY")
    print("=" * 52)
    print(f"  Total new members joined     : {df['new_members'].sum()}")
    print(f"  Peak monthly new members     : {df['new_members'].max()} ({df.loc[df['new_members'].idxmax(), 'month']})")
    print(f"  Total issues opened          : {df['issues_opened'].sum()}")
    print(f"  Total issues closed          : {df['issues_closed'].sum()}")
    print(f"  Avg issue resolution rate    : {df['issue_resolution_rate'].mean():.1f}%")
    print(f"  Total community events held  : {df['events_held'].sum()}")
    print(f"  Avg active contributors/month: {df['active_contributors'].mean():.1f}")
    print("=" * 52)
    print()
    print(df[["month", "new_members", "active_contributors",
              "issues_opened", "issues_closed",
              "issue_resolution_rate", "events_held"]].to_string(index=False))
    print()


# ── Visualisation ─────────────────────────────────────────────────────────────

def plot_dashboard(df, cumulative_members, output_dir="."):
    fig, axes = plt.subplots(2, 2, figsize=(14, 9))
    fig.suptitle("Open Source Community Health Dashboard", fontsize=16, fontweight="bold", y=0.98)
    fig.patch.set_facecolor("#F8F9FA")

    colors = {"blue": "#2E75B6", "green": "#28A745", "orange": "#FD7E14", "red": "#DC3545"}

    months = df["month"]

    # -- Plot 1: Member Growth (bar + cumulative line) --
    ax1 = axes[0, 0]
    ax1.bar(months, df["new_members"], color=colors["blue"], alpha=0.8, label="New Members")
    ax1b = ax1.twinx()
    ax1b.plot(months, cumulative_members, color=colors["orange"], marker="o",
              linewidth=2, markersize=5, label="Cumulative")
    ax1.set_title("Member Growth", fontweight="bold")
    ax1.set_ylabel("New Members / Month", color=colors["blue"])
    ax1b.set_ylabel("Cumulative Members", color=colors["orange"])
    ax1.set_facecolor("#FDFDFD")
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax1b.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, fontsize=8, loc="upper left")

    # -- Plot 2: Issue Resolution Rate --
    ax2 = axes[0, 1]
    ax2.plot(months, df["issue_resolution_rate"], color=colors["green"],
             marker="s", linewidth=2.5, markersize=6)
    ax2.axhline(y=90, color="gray", linestyle="--", linewidth=1, alpha=0.6, label="90% target")
    ax2.fill_between(months, df["issue_resolution_rate"], alpha=0.15, color=colors["green"])
    ax2.set_title("Issue Resolution Rate (%)", fontweight="bold")
    ax2.set_ylabel("Resolution Rate (%)")
    ax2.set_ylim(50, 105)
    ax2.yaxis.set_major_formatter(mticker.PercentFormatter())
    ax2.set_facecolor("#FDFDFD")
    ax2.legend(fontsize=8)

    # -- Plot 3: Active Contributors vs New Members --
    ax3 = axes[1, 0]
    x = range(len(months))
    width = 0.4
    ax3.bar([i - width/2 for i in x], df["new_members"],
            width=width, color=colors["blue"], alpha=0.8, label="New Members")
    ax3.bar([i + width/2 for i in x], df["active_contributors"],
            width=width, color=colors["green"], alpha=0.8, label="Active Contributors")
    ax3.set_title("New Members vs Active Contributors", fontweight="bold")
    ax3.set_ylabel("Count")
    ax3.set_xticks(list(x))
    ax3.set_xticklabels(months)
    ax3.set_facecolor("#FDFDFD")
    ax3.legend(fontsize=8)

    # -- Plot 4: Events Held per Month --
    ax4 = axes[1, 1]
    ax4.bar(months, df["events_held"], color=colors["orange"], alpha=0.85)
    for i, v in enumerate(df["events_held"]):
        ax4.text(i, v + 0.05, str(v), ha="center", va="bottom", fontsize=9, fontweight="bold")
    ax4.set_title("Community Events Held", fontweight="bold")
    ax4.set_ylabel("Number of Events")
    ax4.set_ylim(0, df["events_held"].max() + 1)
    ax4.set_facecolor("#FDFDFD")

    plt.tight_layout(rect=[0, 0, 1, 0.96])

    output_path = os.path.join(output_dir, "community_health_dashboard.png")
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    print(f"Dashboard saved to: {output_path}")
    plt.show()


# ── Run ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print_summary(df)
    plot_dashboard(df, cumulative_members)
