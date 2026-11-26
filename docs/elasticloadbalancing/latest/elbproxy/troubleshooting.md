---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/troubleshooting.html
---

# Troubleshoot ELB for Envoy

Use this chapter to diagnose and fix common issues with your Elastic Load Balancing for Envoy (ELB for Envoy) proxies. The following table lists a symptom, its likely cause, and the fix.

| Symptom | Cause | Fix |
| --- | --- | --- |
| No logs appear in CloudWatch Logs. | The proxy role can't write to the `/aws/elb-proxy/*` log groups, or your Amazon VPC has no network path to CloudWatch Logs. | Grant the proxy role permission to write to the log groups. For more information, see [Create a proxy role](setting-up.md#setting-up-proxy-role). Provide a network path to CloudWatch Logs with an internet gateway or an Amazon VPC endpoint. |
| The proxy state is `create-failed` or `action-required`. | The `status.reasons` field describes the problem.<br />One cause is a customer managed key that ELB for Envoy can't use (reason `CustomerKmsKeyInaccessible`). Another common cause is a configuration that Envoy rejected (reason `InvalidCustomerConfigurationContents`). For more information, see [When ELB for Envoy can't use your key](proxy-encryption.md#proxy-encryption-key-inaccessible) and [action-required reasons](how-proxies-work.md#how-proxies-work-action-required). | Run **aws elb-proxy get-proxy** and read the `status.reasons` field. For more information about proxy states, see [Proxy states](how-proxies-work.md#how-proxies-work-states). |
| `CreateProxy` or `UpdateProxyConfiguration` returns a `ValidationException` that names a field. | The configuration file doesn't match the Envoy schema for the proxy version. | Fix the named field and submit again. For more information, see [Configuration validation](how-envoy-runs.md#how-envoy-runs-validation). |
| An updated configuration doesn't take effect. | The configuration failed the second validation stage (`envoy --mode validate`) and wasn't applied. The previous configuration keeps serving traffic. | Fix the configuration and run the update again. For more information, see [Configuration validation](how-envoy-runs.md#how-envoy-runs-validation). |
| A customer managed key error occurs. | The key errors table describes the cause. | For the cause and fix, see [Errors](proxy-encryption.md#proxy-encryption-errors). |
| Requests to a Lambda function return `403`. | The proxy role lacks the `lambda:InvokeFunction` permission on the function. | Add the permission to the proxy role. For more information, see [Permissions](invoke-lambda.md#invoke-lambda-permissions). |
| Requests are blocked when AWS WAF is unavailable. | The `waf.fail_open.enabled` attribute is `false`, which is the default. | Set `waf.fail_open.enabled` to `true` if you prefer to allow traffic when AWS WAF is unavailable. For more information, see [Allow traffic when AWS WAF is unavailable](waf.md#waf-fail-open). |
| You can't delete a proxy. | Deletion protection is turned on for the proxy. | Turn off deletion protection, and then delete the proxy. For more information, see [Proxy attributes](proxy-attributes.md). |
