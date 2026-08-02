---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/error-handling.html
---

# Error handling
<a name="error-handling"></a>

 The Media2Cloud on AWS solution applies a catch and retry concept for [error handling](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html) to the state machines to improve the resiliency of the solution by retrying the state run multiple times. When the state run exhausts the retries, it stops the run and generates an error.

 The solution also uses [Amazon CloudWatch Events](https://docs.aws.amazon.com/step-functions/latest/dg/cw-events.html) to respond to run errors caused by the state machines (ingestion and analysis). The Lambda error handling function processes the error by analyzing the run history of the failed state machine and sends an Amazon SNS notification to subscribers.
