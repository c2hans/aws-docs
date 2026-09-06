---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/kotlin_1_xray_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# X-Ray examples using SDK for Kotlin
<a name="kotlin_1_xray_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Kotlin with X-Ray.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `CreateGroup`
<a name="xray_CreateGroup_kotlin_1_topic"></a>

The following code example shows how to use `CreateGroup`.

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

### `CreateSamplingRule`
<a name="xray_CreateSamplingRule_kotlin_1_topic"></a>

The following code example shows how to use `CreateSamplingRule`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/xray#code-examples).

```
suspend fun createRule(ruleNameVal: String?) {
    val rule =
        SamplingRule {
            ruleName = ruleNameVal
            priority = 1
            httpMethod = "*"
            serviceType = "*"
            serviceName = "*"
            urlPath = "*"
            version = 1
            host = "*"
            resourceArn = "*"
        }

    val ruleRequest =
        CreateSamplingRuleRequest {
            samplingRule = rule
        }

    XRayClient.fromEnvironment { region = "us-east-1" }.use { xRayClient ->
        val ruleResponse: CreateSamplingRuleResponse = xRayClient.createSamplingRule(ruleRequest)
        println("The ARN of the new rule is ${ruleResponse.samplingRuleRecord?.samplingRule?.ruleArn}")
    }
}
```
+  For API details, see [CreateSamplingRule](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `DeleteGroup`
<a name="xray_DeleteGroup_kotlin_1_topic"></a>

The following code example shows how to use `DeleteGroup`.

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

### `DeleteSamplingRule`
<a name="xray_DeleteSamplingRule_kotlin_1_topic"></a>

The following code example shows how to use `DeleteSamplingRule`.

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

### `GetGroups`
<a name="xray_GetGroups_kotlin_1_topic"></a>

The following code example shows how to use `GetGroups`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/xray#code-examples).

```
suspend fun getAllGroups() {
    XRayClient.fromEnvironment { region = "us-east-1" }.use { xRayClient ->
        val response = xRayClient.getGroups(GetGroupsRequest {})
        response.groups?.forEach { group ->
            println("The AWS X-Ray group name is ${group.groupName}")
        }
    }
}
```
+  For API details, see [GetGroups](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `GetSamplingRules`
<a name="xray_GetSamplingRules_kotlin_1_topic"></a>

The following code example shows how to use `GetSamplingRules`.

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

### `GetServiceGraph`
<a name="xray_GetServiceGraph_kotlin_1_topic"></a>

The following code example shows how to use `GetServiceGraph`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/xray#code-examples).

```
suspend fun getGraph(groupNameVal: String?) {
    val time = aws.smithy.kotlin.runtime.time.Instant
    val getServiceGraphRequest =
        GetServiceGraphRequest {
            groupName = groupNameVal
            this.startTime = time.now()
            endTime = time.now()
        }
    XRayClient.fromEnvironment { region = "us-east-1" }.use { xRayClient ->
        val response = xRayClient.getServiceGraph(getServiceGraphRequest)
        response.services?.forEach { service ->
            println("The name of the service is  ${service.name}")
        }
    }
}
```
+  For API details, see [GetServiceGraph](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.
