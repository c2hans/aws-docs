---
source_url: https://docs.aws.amazon.com/comprehend/latest/dg/realtime-pii-console.html
---

# PII real-time analysis (Console)
<a name="realtime-pii-console"></a>

You can use the console to run PII real-time detection of a text document. The maximum text size is 100 kilobytes of UTF-8 encoded characters. The console displays the results so that you can review the analysis.

**Run PII detection real-time analysis using the built-in model**

1. Sign in to the AWS Management Console and open the Amazon Comprehend console at [https://console.aws.amazon.com/comprehend/](https://console.aws.amazon.com/comprehend/)

1. From the left menu, choose **Real-time analysis**.

1. Under **Input type**, choose **Built-in** for **Analysis type**.

1. Enter the text you want to analyze.

1. Choose **Analyze**. The console displays the text analysis results in the **Insights** panel. The **PII** tab lists the PII entities detected in your input text.

In the **Insights** panel, the **PII** tab displays results for two analysis modes:
+ **Offsets** – identifies the location of PII in the text document.
+ **Labels** – identifies the labels of identified PII entity types.

## Offsets
<a name="realtime-analysis-console-pii-offsets"></a>

The **Offsets** analysis mode identifies the location of PII in your text documents. For more information, see [Locate PII entities](how-pii.md#how-pii-locate).

![The PII offsets analysis mode.](http://docs.aws.amazon.com/comprehend/latest/dg/images/gs-console-pii.png)

## Labels
<a name="realtime-analysis-console-pii-labels"></a>

The **Labels** analysis mode returns the labels of identified PII entity types. For more information, see [Labeling PII entities](how-pii-labels.md).

![The PII labels analysis mode.](http://docs.aws.amazon.com/comprehend/latest/dg/images/gs-console-pii-labels.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
