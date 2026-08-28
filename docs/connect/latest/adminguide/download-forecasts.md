---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/download-forecasts.html
---

# Download a forecast from Connect Customer to view offline
<a name="download-forecasts"></a>

You can download a forecast so you can inspect it offline. A forecast is downloaded as a .csv file of the forecast data. It has the queue name, channel type, timestamp, incoming contact volume and average handle time data.

1. Log in to the Connect Customer admin website with an account that has security profile permissions for **Analytics**, **Forecasting - Edit**.

   For more information, see [Assign permissions](required-optimization-permissions.md).

1. On the Connect Customer navigation menu, choose **Analytics and optimization**, **Forecasting**.

1. On the **Forecasts** tab, choose the forecast.

1. Choose **Actions**, and then download either the last computed forecast or the last published forecast.

1. We recommend choosing **choose here**. This enables you to choose the name of the file download and where to save it, as shown in the following image. Otherwise, the file is saved to your **Downloads** folder and its name is a generated number.
![Forecast page, the choose here button to start downloading a forecast, open with Excel.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-forecasting-download.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
