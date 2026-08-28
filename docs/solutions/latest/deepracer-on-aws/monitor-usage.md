---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/monitor-usage.html
---

# Monitor usage
<a name="monitor-usage"></a>

![Monitor usage](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_resource_usage.png)

The usage graph on the home page shows how many **compute hours** you’ve used out of the number of compute hours that you’ve been allowed to use. Training and evaluating models on DeepRacer on AWS requires compute power, which is provided by Amazon SageMaker AI training jobs. Compute usage is measured in hours, and is accrued as-you-go.

Depending on the configuration selected by your admin, you may have either been given a certain number of hours that you can use, or you may have unlimited hours. Compute hours are accrued throughout a given month, and are reset at the beginning of a new month.

If you exceed or are close to exceeding the number of compute hours that you’ve been allowed, you will need to reach out to your admin to see if more can be allocated.

Under the graph, you can see your current **model storage** defined by the number of models you currently have stored on the instance over the total number you can store. If your admin has not set a limit on the number of models you can store, you will see **Unlimited** for the model count.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
