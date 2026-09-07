---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/monitor-usage.html
---

# Monitor usage
<a name="monitor-usage"></a>

![Monitor usage](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_resource_usage.png)

The usage graph on the home page shows how many **compute hours** you’ve used out of the number of compute hours that you’ve been allowed to use. Training and evaluating models on DeepRacer on AWS requires compute power, which is provided by Amazon SageMaker AI training jobs. Compute usage is measured in hours, and is accrued as-you-go.

Depending on the configuration selected by your admin, you may have either been given a certain number of hours that you can use, or you may have unlimited hours. Compute hours are accrued throughout a given month, and are reset at the beginning of a new month.

If you exceed or are close to exceeding the number of compute hours that you’ve been allowed, you will need to reach out to your admin to see if more can be allocated.

Under the graph, you can see your current **model storage** defined by the number of models you currently have stored on the instance over the total number you can store. If your admin has not set a limit on the number of models you can store, you will see **Unlimited** for the model count.
