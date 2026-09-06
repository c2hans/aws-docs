---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/xray_example_xray_DeleteGroup_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteGroup` with an AWS SDK or CLI
<a name="xray_example_xray_DeleteGroup_section"></a>

The following code examples show how to use `DeleteGroup`.

------
#### [ CLI ]

**AWS CLI**
**To delete a group**
The following `delete-group` example deletes the specified group resource.

```
aws xray delete-group \
    --group-name {{"AdminGroup"}} \
    --group-arn {{"arn:aws:xray:us-east-2:123456789012:group/AdminGroup/123456789"}}
```
This command produces no output.
For more information, see [Configuring Sampling, Groups, and Encryption Settings with the AWS X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-configuration.html#xray-api-configuration-sampling) in the *AWS X-Ray Developer Guide*.
+  For API details, see [DeleteGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/delete-group.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/xray#code-examples).

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.xray.XRayClient;
import software.amazon.awssdk.services.xray.model.DeleteGroupRequest;
import software.amazon.awssdk.services.xray.model.XRayException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class DeleteGroup {
    public static void main(String[] args) {
        final String usage = """

                Usage:    <groupName>

                Where:
                   groupName - The name of the group to delete\s

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

        deleteSpecificGroup(xRayClient, groupName);
    }

    public static void deleteSpecificGroup(XRayClient xRayClient, String groupName) {
        try {
            DeleteGroupRequest groupRequest = DeleteGroupRequest.builder()
                    .groupName(groupName)
                    .build();

            xRayClient.deleteGroup(groupRequest);
            System.out.println(groupName + " was deleted!");

        } catch (XRayException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }
}
```
+  For API details, see [DeleteGroup](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/DeleteGroup) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Kotlin ]

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/xray#code-examples).

```
suspend fun deleteSpecificGroup(groupNameVal: String) {
    val groupRequest =
        DeleteGroupRequest {
            groupName = groupNameVal
        }

    XRayClient.fromEnvironment { region = "us-east-1" }.use { xRayClient ->
        xRayClient.deleteGroup(groupRequest)
        println("$groupNameVal was deleted!")
    }
}
```
+  For API details, see [DeleteGroup](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

------
