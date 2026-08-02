---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/xray_example_xray_GetSamplingRules_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetSamplingRules` with an AWS SDK or CLI
<a name="xray_example_xray_GetSamplingRules_section"></a>

The following code examples show how to use `GetSamplingRules`.

------
#### [ CLI ]

**AWS CLI**
**To retrieve all sampling rules**
The following `get-sampling-rules` example displays details for all available sampling rules.:

```
aws xray get-sampling-rules
```
Output:

```
{
    "SamplingRuleRecords": [
        {
            "SamplingRule": {
                "RuleName": "Default",
                "RuleARN": "arn:aws:xray:us-east-1::sampling-rule/Default",
                "ResourceARN": "*",
                "Priority": 10000,
                "FixedRate": 0.01,
                "ReservoirSize": 0,
                "ServiceName": "*",
                "ServiceType": "*",
                "Host": "*",
                "HTTPMethod": "*",
                "URLPath": "*",
                "Version": 1,
                "Attributes": {}
            },
            "CreatedAt": 0.0,
            "ModifiedAt": 1530558121.0
        },
        {
            "SamplingRule": {
                "RuleName": "base-scorekeep",
                "RuleARN": "arn:aws:xray:us-east-1::sampling-rule/base-scorekeep",
                "ResourceARN": "*",
                "Priority": 9000,
                "FixedRate": 0.1,
                "ReservoirSize": 2,
                "ServiceName": "Scorekeep",
                "ServiceType": "*",
                "Host": "*",
                "HTTPMethod": "*",
                "URLPath": "*",
                "Version": 1,
                "Attributes": {}
            },
            "CreatedAt": 1530573954.0,
            "ModifiedAt": 1530920505.0
        },
        {
            "SamplingRule": {
                "RuleName": "polling-scorekeep",
                "RuleARN": "arn:aws:xray:us-east-1::sampling-rule/polling-scorekeep",
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
            "CreatedAt": 1530918163.0,
            "ModifiedAt": 1530918163.0
        }
    ]
}
```
For more information, see [Using Sampling Rules with the X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-sampling.html) in the *AWS X-Ray Developer Guide*.
+  For API details, see [GetSamplingRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-sampling-rules.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/xray#code-examples).

```
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.xray.XRayClient;
import software.amazon.awssdk.services.xray.model.GetSamplingRulesResponse;
import software.amazon.awssdk.services.xray.model.SamplingRuleRecord;
import software.amazon.awssdk.services.xray.model.XRayException;
import java.util.List;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class GetSamplingRules {
    public static void main(String[] args) {
        Region region = Region.US_EAST_1;
        XRayClient xRayClient = XRayClient.builder()
                .region(region)
                .credentialsProvider(ProfileCredentialsProvider.create())
                .build();

        getRules(xRayClient);
    }

    public static void getRules(XRayClient xRayClient) {
        try {
            GetSamplingRulesResponse response = xRayClient.getSamplingRules(r -> r.build());
            List<SamplingRuleRecord> records = response.samplingRuleRecords();

            for (SamplingRuleRecord record : records) {
                System.out.println("The rule name is: " + record.samplingRule().ruleName());
                System.out.println("The related service is: " + record.samplingRule().serviceName());
            }
        } catch (XRayException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }
}
```
+  For API details, see [GetSamplingRules](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetSamplingRules) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Kotlin ]

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/xray#code-examples).

```
suspend fun getRules() {
    XRayClient.fromEnvironment { region = "us-east-1" }.use { xRayClient ->
        val response = xRayClient.getSamplingRules(GetSamplingRulesRequest {})
        response.samplingRuleRecords?.forEach { record ->
            println("The rule name is ${record.samplingRule?.ruleName}")
            println("The related service is: ${record.samplingRule?.serviceName}")
        }
    }
}
```
+  For API details, see [GetSamplingRules](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

------
