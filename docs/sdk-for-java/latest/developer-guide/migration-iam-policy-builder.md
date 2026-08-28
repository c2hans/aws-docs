---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-iam-policy-builder.html
---

# Changes in the IAM Policy Builder API from version 1 to version 2
<a name="migration-iam-policy-builder"></a>

This topic details the changes in the IAM Policy Builder API from version 1 (v1) to version 2 (v2).

## High-level changes
<a name="migration-iam-policy-builder-high-level"></a>

| Change | v1 | v2 |
| --- | --- | --- |
|  <br />Maven dependencies |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>com.amazonaws</groupId><br />            <artifactId>aws-java-sdk-bom</artifactId><br />            <version>{{1.12.5871}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>com.amazonaws</groupId><br />        <artifactId>aws-java-sdk-core</artifactId><br />    </dependency><br /></dependencies></pre>  |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>software.amazon.awssdk</groupId><br />            <artifactId>bom</artifactId><br />            <version>{{2.27.212}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>software.amazon.awssdk</groupId><br />        <artifactId>iam-policy-builder</artifactId><br />    </dependency><br /></dependencies></pre>  |
| Package name | com.amazonaws.auth.policy | software.amazon.awssdk.policybuilder.iam |
| Class names | [Policy](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/Policy.html)<br />[Statement](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/Statement.html)+  [Statement.Effect](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/Statement.Effect.html) <br />+  [IdentiyManagementActions](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/actions/IdentityManagementActions.html) <br />+  [Resource](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/Resource.html) <br />+  [Principal](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/Principal.html) <br />+  [Condition](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/Condition.html)  | [IamPolicy](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamPolicy.html)<br />[IamStatement](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamStatement.html)+  [IamEffect](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamEffect.html) <br />+  [IamAction](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamAction.html) <br />+  [IamResource](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamResource.html) <br />+  [IamPrincipal](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamPrincipal.html) <br />+  [IamCondition](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamCondition.html) <br />+  [IamConditionOperator](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamConditionOperator.html) <br />+  [IamConditionKey](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamConditionKey.html)  |

1 [Latest version](https://central.sonatype.com/artifact/com.amazonaws/aws-java-sdk-bom). 2 [Latest version](https://central.sonatype.com/artifact/software.amazon.awssdk/bom).

## API changes
<a name="migration-iam-policy-builder-api"></a>

| Setting | v1 | v2 |
| --- | --- | --- |
|  Instantiate a policy |  <pre>Policy policy = new Policy();</pre>  |  <pre>IamPolicy.Builder policyBuilder = IamPolicy.builder();<br />...<br />IamPolicy policy = policyBuilder.build();</pre>  |
|  <br />Set id |  <pre>policy.withtId(...);<br />policy.setId(...);</pre>  |  <pre>policyBuilder.id(...);</pre>  |
|  <br />Set version | N/A - uses default version of 2012-10-17 |  <pre>policyBuilder.version(...);</pre>  |
|  <br />Create statement |  <pre>Statement statement = <br />    new Statement(Effect.Allow)<br />            .withActions(...)<br />            .withConditions(...)<br />            .withId(...)<br />            .withPrincipals(...)<br />            .withResources(...);</pre>  |  <pre>IamStatement statement = <br />    IamStatement.builder()<br />            .effect(IamEffect.ALLOW)<br />            .actions(...)<br />            .notActions(...)<br />            .conditions(...)<br />            .sid(...)<br />            .principals(...)<br />            .notPrincipals(...)<br />            .resources(...)<br />            .notResources(...)<br />            .build()</pre>  |
|  <br />Set statement |  <pre>policy.withStatements(statement);<br />policy.setStatements(statement);</pre>  |  <pre>policyBuilder.addStatement(statement);</pre>  |

## Differences in building a statement
<a name="migration-iam-policy-builder-statement"></a>

### Actions
<a name="migration-iam-policy-builder-statement-actions"></a>

#### v1
<a name="migration-iam-policy-builder-statement-actions.v1"></a>

The v1 SDK has [`enum` types](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/Action.html) for service actions that represent `[*Action*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_action.html)` elements in a policy statement. The following `enum` types are some examples.
+ `[IdentityManagementActions](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/actions/IdentityManagementActions.html)`
+ `[DynamoDBv2Actions](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/actions/DynamoDBv2Actions.html)`
+ `[SQSActions](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/actions/SQSActions.html)`

The following example shows the `SendMessage` constant for `SQSActions`.

```
Action action = SQSActions.SendMessage;
```

You cannot specify a `[*NotAction*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notaction.html)` element to a statement in v1.

#### v2
<a name="migration-iam-policy-builder-statement-actions.v2"></a>

In v2, the [IamAction](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamAction.html) interface represents all actions. To specify a [service-specific action](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_action.html) element, pass a string to the `create` method as shown in the following code.

```
IamAction action = IamAction.create("sqs:SendMessage");
```

You can specify a `[*NotAction*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notaction.html)` for a statement with v2 as shown in the following code.

```
IamAction action = IamAction.create("sqs:SendMessage");
IamStatement.builder().addNotAction(action);
```

### Conditions
<a name="migration-iam-policy-builder-statement-conditions"></a>

#### v1
<a name="migration-iam-policy-builder-statement-conditions-v1"></a>

To represent statement conditions, the v1 SDK uses subclasses of [`Condition`](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/Condition.html).
+  [ArnCondition](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/conditions/ArnCondition.html)
+  [BooleanCondition](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/conditions/BooleanCondition.html)
+  [DateCondition](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/conditions/DateCondition.html)
+ [IpAddressCondition](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/conditions/IpAddressCondition.html)
+ [NumericCondition](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/conditions/NumericCondition.html)
+ [ StringCondition ](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/conditions/StringCondition.html)

Each `Condition` subclass defines a comparison `enum` type to help define the condition. For example, the following shows a *not like*[ string comparison](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_String) for a condition.

```
Condition condition = new StringCondition(StringComparisonType.StringNotLike, "key", "value");
```

#### v2
<a name="migration-iam-policy-builder-statement-conditions-v2"></a>

In v2, you build a condition for a policy statement by using `[IamCondition](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamCondition.html)` and provide an `[IamConditionOperator](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamConditionOperator.html)`, which contains `enums` for all types.

```
IamCondition condition = IamCondition.create(IamConditionOperator.STRING_NOT_LIKE, "key", "value");
```

### Resources
<a name="migration-iam-policy-builder-statement-resources"></a>

#### v1
<a name="migration-iam-policy-builder-statement-resources-v1"></a>

A policy statement's `[*Resource*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html)` element is represented by the SDK's `[Resource](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/Resource.html)` class. You supply the ARN as a string in the constructor. The following subclasses provide convenience constructors.
+ [S3BucketResource](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/resources/S3BucketResource.html)
+ [S3ObjectResource](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/resources/S3ObjectResource.html)
+ [SQSQueueResource](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/resources/SQSQueueResource.html)

In v1, you can specify a `[*NotResource*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notresource.html)` element for a `[Resource](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/Resource.html)` by calling the `withIsNotType` method as shown in the following statement.

```
Resource resource = new Resource("arn:aws:s3:::amzn-s3-demo-bucket").withIsNotType(true);
```

#### v2
<a name="migration-iam-policy-builder-statement-resources-v2"></a>

In v2, you create a `[*Resource*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html)` element by passing an ARN to the `IamResource.create` method.

```
IamResource resource = IamResource.create("arn:aws:s3:::amzn-s3-demo-bucket");
```

An `[IamResource](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamResource.html)` can be set as *[`NotResource`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notresource.html)* element as shown in the following snippet.

```
IamResource resource = IamResource.create("arn:aws:s3:::amzn-s3-demo-bucket");
IamStatement.builder().addNotResource(resource);
```

`IamResource.ALL` represents all resources.

### Principals
<a name="migration-iam-policy-builder-statement-principal"></a>

#### v1
<a name="migration-iam-policy-builder-statement-principal-v1"></a>

The v1 SDK offers the following `[Principal](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/policy/Principal.html)` classes to represent types of principals that include all members:
+ `AllUsers`
+ `AllServices`
+ `AllWebProviders`
+ `All`

You cannot add a `[*NotPrincipal*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notprincipal.html)` element to a statement.

#### v2
<a name="migration-iam-policy-builder-statement-principal-v2"></a>

In v2, `IamPrincipal.ALL` represents all principals:

To represent all members in other types of principals, use the `[IamPrincipalType](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamPrincipalType.html)` classes when you create a `IamPrincipal`.
+ `IamPrincipal.create(IamPrincipalType.AWS,"*")` for all users.
+ `IamPrincipal.create(IamPrincipalType.SERVICE,"*")` for all services.
+ `IamPrincipal.create(IamPrincipalType.FEDERATED,"*")` for all web providers.
+ `IamPrincipal.create(IamPrincipalType.CANONICAL_USER,"*")` for all canonical users.

You can use the `addNotPrincipal` method to represent a `[*NotPrincipal*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notprincipal.html)` element when you create a policy statement as shown in the following statement.

```
IamPrincipal principal = IamPrincipal.create(IamPrincipalType.AWS, "arn:aws:iam::444455556666:root");
IamStatement.builder().addNotPrincipal(principal);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
