
----------------------------------
Community Health Tracker

A Python tool for tracking and visualising key health metrics for open source communities.
Built with real community management work in mind — the kind of metrics that matter when you are running contributor programs, managing onboarding, and reporting community growth to stakeholders.

---------------------------------
What it tracks

This tool monitors six core metrics that reflect the health and growth of an open source community.
New members tracks how many people join each month, giving a clear picture of growth momentum. Active contributors goes a step further, counting only members who are making meaningful contributions rather than just passively observing. Together, these two numbers reveal the quality of growth, not just the quantity.
On the activity side, the tracker records issues opened and closed each month to measure workload and resolution velocity, and calculates the issue resolution rate as a percentage of issues closed. This tells you whether the team is keeping up with incoming work or falling behind.
Finally, events held logs community calls, collaboration cafes, and workshops across the year, while cumulative growth maintains a running total of all members who have joined since tracking began.

Output
Running the script prints a full year summary to the console and generates a 4-panel dashboard chart saved as community_health_dashboard.png.

====================================================
   COMMUNITY HEALTH REPORT — FULL YEAR SUMMARY
====================================================
  Total new members joined     : 393
  Peak monthly new members     : 60 (Dec)
  Total issues opened          : 246
  Total issues closed          : 220
  Avg issue resolution rate    : 89.3%
  Total community events held  : 34
  Avg active contributors/month: 16.2
====================================================

