---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ecs_example_ecs_DeleteService_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteService` with an AWS SDK or CLI
<a name="ecs_example_ecs_DeleteService_section"></a>

The following code examples show how to use `DeleteService`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Configure container service connectivity](ecs_example_ecs_ServiceConnect_085_section.md)
+  [Create a container task for the serverless launch type](ecs_example_ecs_GettingStarted_086_section.md)
+  [Creating a container service for virtual machine instances](ecs_example_ecs_GettingStarted_018_section.md)

------
#### [ CLI ]

**AWS CLI**
**To delete a service**
The following `ecs delete-service` example deletes the specified service from a cluster. You can include the `--force` parameter to delete a service even if it has not been scaled to zero tasks.

```
aws ecs delete-service --cluster {{MyCluster}} --service {{MyService1}} --force
```
For more information, see [Deleting a Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/delete-service.html) in the *Amazon ECS Developer Guide*.
+  For API details, see [DeleteService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/delete-service.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecs#code-examples).

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ecs.EcsClient;
import software.amazon.awssdk.services.ecs.model.DeleteServiceRequest;
import software.amazon.awssdk.services.ecs.model.EcsException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */

public class DeleteService {
    public static void main(String[] args) {
        final String usage = """

                Usage:
                  <clusterName> <serviceArn>\s

                Where:
                  clusterName - The name of the ECS cluster.
                  serviceArn - The ARN of the ECS service.
                """;

        if (args.length != 2) {
            System.out.println(usage);
            System.exit(1);
        }

        String clusterName = args[0];
        String serviceArn = args[1];
        Region region = Region.US_EAST_1;
        EcsClient ecsClient = EcsClient.builder()
                .region(region)
                .build();

        deleteSpecificService(ecsClient, clusterName, serviceArn);
        ecsClient.close();
    }

    public static void deleteSpecificService(EcsClient ecsClient, String clusterName, String serviceArn) {
        try {
            DeleteServiceRequest serviceRequest = DeleteServiceRequest.builder()
                    .cluster(clusterName)
                    .service(serviceArn)
                    .build();

            ecsClient.deleteService(serviceRequest);
            System.out.println("The Service was successfully deleted");

        } catch (EcsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}
```
+  For API details, see [DeleteService](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DeleteService) in *AWS SDK for Java 2.x API Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Deletes the service named 'my-http-service' in the default cluster. The service must have a desired count and running count of 0 before you can delete it. You are prompted for confirmation before the command proceeds. To bypass the confirmation prompt add the -Force switch.**

```
Remove-ECSService -Service my-http-service
```
**Example 2: Deletes the service named 'my-http-service' in the named cluster.**

```
Remove-ECSService -Cluster myCluster -Service my-http-service
```
+  For API details, see [DeleteService](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Deletes the service named 'my-http-service' in the default cluster. The service must have a desired count and running count of 0 before you can delete it. You are prompted for confirmation before the command proceeds. To bypass the confirmation prompt add the -Force switch.**

```
Remove-ECSService -Service my-http-service
```
**Example 2: Deletes the service named 'my-http-service' in the named cluster.**

```
Remove-ECSService -Cluster myCluster -Service my-http-service
```
+  For API details, see [DeleteService](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
