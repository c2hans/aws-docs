---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/xray_example_xray_DeleteSamplingRule_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteSamplingRule` with an AWS SDK or CLI
<a name="xray_example_xray_DeleteSamplingRule_section"></a>

The following code examples show how to use `DeleteSamplingRule`.

------
#### [ CLI ]

**AWS CLI**
**To delete a sampling rule**
The following `delete-sampling-rule` example deletes the specified sampling rule. You can specify the group by using either the group name or group ARN.

```
aws xray delete-sampling-rule \
    --rule-name {{polling-scorekeep}}
```
Output:

```
{
    "SamplingRuleRecord": {
        "SamplingRule": {
            "RuleName": "polling-scorekeep",
            "RuleARN": "arn:aws:xray:us-west-2:123456789012:sampling-rule/polling-scorekeep",
            "ResourceARN": "*",
            "Priority": 5000,
            "FixedRate": 0.003,
            "ReservoirSize": 0,
            "ServiceName": "Scorekeep",
            "ServiceType": "*",
            "Host": "*",
            "HTTPMethod": "GET",
            "URLPath": "/api/state/*",
            "Version": 1,
            "Attributes": {}
        },
        "CreatedAt": 1530574399.0,
        "ModifiedAt": 1530574399.0
    }
}
```
For more information, see [Configuring Sampling, Groups, and Encryption Settings with the AWS X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-configuration.html#xray-api-configuration-sampling) in the *AWS X-Ray Developer Guide*.
+  For API details, see [DeleteSamplingRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/delete-sampling-rule.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/xray#code-examples).

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.xray.XRayClient;
import software.amazon.awssdk.services.xray.model.DeleteSamplingRuleRequest;
import software.amazon.awssdk.services.xray.model.XRayException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class DeleteSamplingRule {
    public static void main(String[] args) {
        final String usage = """

                Usage:    <ruleName>

                Where:
                   ruleName - The name of the rule to delete\s

                """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String ruleName = args[0];
        Region region = Region.US_EAST_1;
        XRayClient xRayClient = XRayClient.builder()
                .region(region)
                .build();

        deleteRule(xRayClient, ruleName);
    }

    public static void deleteRule(XRayClient xRayClient, String ruleName) {
        try {
            DeleteSamplingRuleRequest ruleRequest = DeleteSamplingRuleRequest.builder()
                    .ruleName(ruleName)
                    .build();

            xRayClient.deleteSamplingRule(ruleRequest);
        } catch (XRayException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }
}
```
+  For API details, see [DeleteSamplingRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/DeleteSamplingRule) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Kotlin ]

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/xray#code-examples).

```
suspend fun deleteRule(ruleNameVal: String?) {
    val ruleRequest =
        DeleteSamplingRuleRequest {
            ruleName = ruleNameVal
        }

    XRayClient.fromEnvironment { region = "us-east-1" }.use { xRayClient ->
        xRayClient.deleteSamplingRule(ruleRequest)
        println("$ruleNameVal was deleted")
    }
}
```
+  For API details, see [DeleteSamplingRule](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

------
