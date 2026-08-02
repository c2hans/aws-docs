---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/xray_example_xray_CreateGroup_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateGroup` with an AWS SDK or CLI
<a name="xray_example_xray_CreateGroup_section"></a>

The following code examples show how to use `CreateGroup`.

------
#### [ CLI ]

**AWS CLI**
**To create a group**
The following `create-group` example creates a group resource named `AdminGroup`. The group gets a filter expression that defines the criteria of the group as a segment related to a specific service causing a fault or an error.

```
aws xray create-group \
   --group-name {{"AdminGroup"}} \
   --filter-expression "service(\"mydomain.com\") {fault OR error}"
```
Output:

```
{
    "GroupName": "AdminGroup",
    "GroupARN": "arn:aws:xray:us-west-2:123456789012:group/AdminGroup/123456789",
    "FilterExpression": "service(\"mydomain.com\") {fault OR error}"
}
```
For more information, see [Configuring Sampling, Groups, and Encryption Settings with the AWS X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-configuration.html#xray-api-configuration-sampling) in the *AWS X-Ray Developer Guide*.
+  For API details, see [CreateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/create-group.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/xray#code-examples).

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.xray.XRayClient;
import software.amazon.awssdk.services.xray.model.CreateGroupRequest;
import software.amazon.awssdk.services.xray.model.CreateGroupResponse;
import software.amazon.awssdk.services.xray.model.XRayException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class CreateGroup {
    public static void main(String[] args) {
        final String usage = """

                Usage:    <groupName>

                Where:
                   groupName - The name of the group to create\s

                """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String groupName = args[0];
        Region region = Region.US_EAST_1;
        XRayClient xRayClient = XRayClient.builder()
                .region(region)
                .build();

        createNewGroup(xRayClient, groupName);
    }

    public static void createNewGroup(XRayClient xRayClient, String groupName) {
        try {
            CreateGroupRequest groupRequest = CreateGroupRequest.builder()
                    .filterExpression("fault = true AND http.url CONTAINS \"example/game\" AND responsetime >= 5")
                    .groupName(groupName)
                    .build();

            CreateGroupResponse groupResponse = xRayClient.createGroup(groupRequest);
            System.out.println("The Group ARN is " + groupResponse.group().groupARN());

        } catch (XRayException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }
}
```
+  For API details, see [CreateGroup](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/CreateGroup) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Kotlin ]

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/xray#code-examples).

```
suspend fun createNewGroup(groupNameVal: String?) {
    val groupRequest =
        CreateGroupRequest {
            filterExpression = "fault = true AND http.url CONTAINS \"example/game\" AND responsetime >= 5"
            groupName = groupNameVal
        }

    XRayClient.fromEnvironment { region = "us-east-1" }.use { xRayClient ->
        val groupResponse = xRayClient.createGroup(groupRequest)
        println("The Group ARN is " + (groupResponse.group?.groupArn))
    }
}
```
+  For API details, see [CreateGroup](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

------
