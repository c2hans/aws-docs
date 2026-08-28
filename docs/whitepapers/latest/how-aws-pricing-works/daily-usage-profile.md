---
source_url: https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/daily-usage-profile.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Daily usage proﬁle
<a name="daily-usage-profile"></a>

 You can monitor daily usage for your application so that you can better estimate your costs. For instance, you can look at the daily pattern to ﬁgure out how your application handles traffic. For each hour, track how many hits you get on your website and how many instances are running, and then add up the total number of hits for that day.

```
 Hourly instance pattern = (hits per hour on website) / (number of instances)
```

 Examine the number of Amazon EC2 instances that run each hour, and then take the average. You can use the number of hits per day and the average number of instances for your calculations.

```
 Daily proﬁle = SUM(Hourly instance pattern) / 24
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
