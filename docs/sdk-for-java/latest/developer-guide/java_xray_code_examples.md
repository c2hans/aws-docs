---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_xray_code_examples.html
---

# X-Ray examples using SDK for Java 2.x
<a name="java_xray_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Java 2.x with X-Ray.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `CreateGroup`
<a name="xray_CreateGroup_java_topic"></a>

The following code example shows how to use `CreateGroup`.

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

### `CreateSamplingRule`
<a name="xray_CreateSamplingRule_java_topic"></a>

The following code example shows how to use `CreateSamplingRule`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/xray#code-examples).

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.xray.XRayClient;
import software.amazon.awssdk.services.xray.model.CreateSamplingRuleRequest;
import software.amazon.awssdk.services.xray.model.SamplingRule;
import software.amazon.awssdk.services.xray.model.XRayException;
import software.amazon.awssdk.services.xray.model.CreateSamplingRuleResponse;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class CreateSamplingRule {
    public static void main(String[] args) {
        final String usage = """

                Usage:    <ruleName>

                Where:
                   ruleName - The name of the rule\s

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

        createRule(xRayClient, ruleName);
    }

    public static void createRule(XRayClient xRayClient, String ruleName) {
        try {

            SamplingRule rule = SamplingRule.builder()
                    .ruleName(ruleName)
                    .priority(1)
                    .httpMethod("*")
                    .serviceType("*")
                    .serviceName("*")
                    .urlPath("*")
                    .version(1)
                    .host("*")
                    .resourceARN("*")
                    .build();

            CreateSamplingRuleRequest ruleRequest = CreateSamplingRuleRequest.builder()
                    .samplingRule(rule)
                    .build();

            CreateSamplingRuleResponse ruleResponse = xRayClient.createSamplingRule(ruleRequest);
            System.out.println(
                    "The ARN of the new rule is " + ruleResponse.samplingRuleRecord().samplingRule().ruleARN());

        } catch (XRayException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }
}
```
+  For API details, see [CreateSamplingRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/CreateSamplingRule) in *AWS SDK for Java 2.x API Reference*.

### `DeleteGroup`
<a name="xray_DeleteGroup_java_topic"></a>

The following code example shows how to use `DeleteGroup`.

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

### `DeleteSamplingRule`
<a name="xray_DeleteSamplingRule_java_topic"></a>

The following code example shows how to use `DeleteSamplingRule`.

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

### `GetGroups`
<a name="xray_GetGroups_java_topic"></a>

The following code example shows how to use `GetGroups`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/xray#code-examples).

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.xray.XRayClient;
import software.amazon.awssdk.services.xray.model.GetGroupsResponse;
import software.amazon.awssdk.services.xray.model.GroupSummary;
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
public class GetGroups {
    public static void main(String[] args) {
        Region region = Region.US_EAST_1;
        XRayClient xRayClient = XRayClient.builder()
                .region(region)
                .build();

        getAllGroups(xRayClient);
    }

    public static void getAllGroups(XRayClient xRayClient) {
        try {
            GetGroupsResponse groupsResponse = xRayClient.getGroups();
            List<GroupSummary> groups = groupsResponse.groups();
            for (GroupSummary group : groups) {
                System.out.println("The AWS XRay group name is " + group.groupName());
            }

        } catch (XRayException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }
}
```
+  For API details, see [GetGroups](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetGroups) in *AWS SDK for Java 2.x API Reference*.

### `GetSamplingRules`
<a name="xray_GetSamplingRules_java_topic"></a>

The following code example shows how to use `GetSamplingRules`.

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

### `GetServiceGraph`
<a name="xray_GetServiceGraph_java_topic"></a>

The following code example shows how to use `GetServiceGraph`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/xray#code-examples).

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.xray.XRayClient;
import software.amazon.awssdk.services.xray.model.GetServiceGraphRequest;
import software.amazon.awssdk.services.xray.model.GetServiceGraphResponse;
import software.amazon.awssdk.services.xray.model.Service;
import software.amazon.awssdk.services.xray.model.XRayException;
import java.time.LocalDateTime;
import java.time.Instant;
import java.time.ZoneId;
import java.util.List;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class GetServiceGraph {
    public static void main(String[] args) {
        final String usage = """

                Usage:    <groupName>

                Where:
                   groupName - The name of a group based on which you want to generate a graph.

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
        getGraph(xRayClient, groupName);
    }

    public static void getGraph(XRayClient xRayClient, String groupName) {
        try {
            // The Instant values have to be 6 hours apart.
            LocalDateTime localDateTime = LocalDateTime.parse("2022-03-09T06:00:00");
            Instant start = localDateTime.atZone(ZoneId.of("America/New_York")).toInstant();

            LocalDateTime localDateTime2 = LocalDateTime.parse("2022-03-09T12:00:00");
            Instant end = localDateTime2.atZone(ZoneId.of("America/New_York")).toInstant();

            GetServiceGraphRequest getServiceGraphRequest = GetServiceGraphRequest.builder()
                    .groupName(groupName)
                    .startTime(start)
                    .endTime(end)
                    .build();

            GetServiceGraphResponse graphResponse = xRayClient.getServiceGraph(getServiceGraphRequest);
            List<Service> services = graphResponse.services();
            for (Service service : services) {
                System.out.println("The name of the service is  " + service.name());
            }

        } catch (XRayException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }
}
```
+  For API details, see [GetServiceGraph](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetServiceGraph) in *AWS SDK for Java 2.x API Reference*.
