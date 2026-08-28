---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-policy-variables.html
---

# AWS IoT Core policy variables
<a name="iot-policy-variables"></a>

AWS IoT Core defines policy variables that can be used in AWS IoT Core policies in the `Resource` or `Condition` block. When a policy is evaluated, the policy variables are replaced by actual values. For example, if a device is connected to the AWS IoT Core message broker with a client ID of 100-234-3456, the `iot:ClientId` policy variable is replaced in the policy document by 100-234-3456.

AWS IoT Core policies can use wildcard characters and follow a similar convention to IAM policies. Inserting an `*` (asterik) in the string can be treated as a wildcard, matching any characters. For example, you can use `*` to describe multiple MQTT topic names in the `Resource` attribute of a policy. The characters `+` and `#` are treated as literal strings in a policy. For an example policy that shows how to use wildcards, see [Using wildcard characters in MQTT and AWS IoT Core policies](pub-sub-policy.md#pub-sub-policy-cert).

You can also use predefined policy variables with fixed values to represent characters that otherwise have special meaning. These special characters include `$(*)`, `$(?)`, and `$($)`. For more information about policy variables and the special characters, see [IAM Policy elements: Variables and tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html) and [Creating a condition with multiple keys or values](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_multi-value-conditions.html).

**Topics**
+ [Basic AWS IoT Core policy variables](basic-policy-variables.md)
+ [Thing policy variables](thing-policy-variables.md)
+ [X.509 Certificate AWS IoT Core policy variables](cert-policy-variables.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
