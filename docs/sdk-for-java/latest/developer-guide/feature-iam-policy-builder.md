---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/feature-iam-policy-builder.html
---

# Create IAM policies with the AWS SDK for Java 2.x
<a name="feature-iam-policy-builder"></a>

The [IAM Policy Builder API](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/package-summary.html) is a library that you can use to build [IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in Java and upload them to AWS Identity and Access Management (IAM).

Instead of building an IAM policy by manually assembling a JSON string or by reading a file, the API provides a client-side, object-oriented approach to generate the JSON string. When you read an existing IAM policy in JSON format, the API converts it to an [IamPolicy](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamPolicy.html) instance for handling.

The IAM Policy Builder API became available with version 2.20.105 of the SDK, so use that version or a later one in your Maven build file. The latest version number of the SDK is [listed on Maven central](https://central.sonatype.com/artifact/software.amazon.awssdk/iam-policy-builder).

The following snippet shows an example dependency block for a Maven `pom.xml` file. This allows you to use the IAM Policy Builder API in your project.

```
<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>iam-policy-builder</artifactId>
    <version>{{2.27.21}}</version>
</dependency>
```

## Create an `IamPolicy`
<a name="iam-policy-builder-create"></a>

This section shows several examples of how to build policies by using the IAM Policy Builder API.

In each of the following examples, start with the `[IamPolicy.Builder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamPolicy.Builder.html)` and add one or more statements by using the `addStatement` method. Following this pattern, the [IamStatement.Builder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/policybuilder/iam/IamStatement.Builder.html) has methods to add the effect, actions, resources, and conditions to the statement.

### Example: Create a time-based policy
<a name="iam-policy-builder-create-ex-time-based"></a>

The following example creates an identity-based policy that permits the Amazon DynamoDB `GetItem` action between two points in time.

```
    public String timeBasedPolicyExample() {
        IamPolicy policy = IamPolicy.builder()
                .addStatement(b -> b
                        .effect(IamEffect.ALLOW)
                        .addAction("dynamodb:GetItem")
                        .addResource(IamResource.ALL)
                        .addCondition(b1 -> b1
                                .operator(IamConditionOperator.DATE_GREATER_THAN)
                                .key("aws:CurrentTime")
                                .value("2020-04-01T00:00:00Z"))
                        .addCondition(b1 -> b1
                                .operator(IamConditionOperator.DATE_LESS_THAN)
                                .key("aws:CurrentTime")
                                .value("2020-06-30T23:59:59Z")))
                .build();

        // Use an IamPolicyWriter to write out the JSON string to a more readable format.
        return policy.toJson(IamPolicyWriter.builder()
                        .prettyPrint(true)
                        .build());
    }
```

#### JSON output
<a name="iam-builder-ex-json-date"></a>

The last statement in the previous example returns the following JSON string.

Read more about this [example](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws-dates.html) in the *AWS Identity and Access Management User Guide*.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Action": "dynamodb:GetItem",
        "Resource": "*",
        "Condition": {
            "DateGreaterThan": {
                "aws:CurrentTime": "2020-04-01T00:00:00Z"
            },
            "DateLessThan": {
                "aws:CurrentTime": "2020-06-30T23:59:59Z"
            }
        }
    }
}
```

------

### Example: Specify multiple conditions
<a name="iam-policy-builder-create-ex-multi-conditions"></a>

The following example shows how you can create an identity-based policy that allows access to specific DynamoDB attributes. The policy contains two conditions.

```
    public String multipleConditionsExample() {
        IamPolicy policy = IamPolicy.builder()
                .addStatement(b -> b
                        .effect(IamEffect.ALLOW)
                        .addAction("dynamodb:GetItem")
                        .addAction("dynamodb:BatchGetItem")
                        .addAction("dynamodb:Query")
                        .addAction("dynamodb:PutItem")
                        .addAction("dynamodb:UpdateItem")
                        .addAction("dynamodb:DeleteItem")
                        .addAction("dynamodb:BatchWriteItem")
                        .addResource("arn:aws:dynamodb:*:*:table/table-name")
                        .addConditions(IamConditionOperator.STRING_EQUALS.addPrefix("ForAllValues:"),
                                "dynamodb:Attributes",
                                List.of("column-name1", "column-name2", "column-name3"))
                        .addCondition(b1 -> b1.operator(IamConditionOperator.STRING_EQUALS.addSuffix("IfExists"))
                                .key("dynamodb:Select")
                                .value("SPECIFIC_ATTRIBUTES")))
                .build();

        return policy.toJson(IamPolicyWriter.builder()
                .prettyPrint(true).build());
    }
```

#### JSON output
<a name="iam-builder-ex-json-multi-cond"></a>

The last statement in the previous example returns the following JSON string.

Read more about this [example](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_dynamodb_attributes.html) in the *AWS Identity and Access Management User Guide*.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Action": [
            "dynamodb:GetItem",
            "dynamodb:BatchGetItem",
            "dynamodb:Query",
            "dynamodb:PutItem",
            "dynamodb:UpdateItem",
            "dynamodb:DeleteItem",
            "dynamodb:BatchWriteItem"
        ],
        "Resource": "arn:aws:dynamodb:*:*:table/table-name",
        "Condition": {
            "ForAllValues:StringEquals": {
                "dynamodb:Attributes": [
                    "column-name1",
                    "column-name2",
                    "column-name3"
                ]
            },
            "StringEqualsIfExists": {
                "dynamodb:Select": "SPECIFIC_ATTRIBUTES"
            }
        }
    }
}
```

------

### Example: Specify principals
<a name="iam-policy-builder-create-ex-principals"></a>

The following example shows how to create a resource-based policy that denies access to a bucket for all principals except for those specified in the condition.

```
    public String specifyPrincipalsExample() {
        IamPolicy policy = IamPolicy.builder()
                .addStatement(b -> b
                        .effect(IamEffect.DENY)
                        .addAction("s3:*")
                        .addPrincipal(IamPrincipal.ALL)
                        .addResource("arn:aws:s3:::BUCKETNAME/*")
                        .addResource("arn:aws:s3:::BUCKETNAME")
                        .addCondition(b1 -> b1
                                .operator(IamConditionOperator.ARN_NOT_EQUALS)
                                .key("aws:PrincipalArn")
                                .value("arn:aws:iam::444455556666:user/user-name")))
                .build();
        return policy.toJson(IamPolicyWriter.builder()
                .prettyPrint(true).build());
    }
```

#### JSON output
<a name="iam-policy-builder-create-json-ex-principals"></a>

The last statement in the previous example returns the following JSON string.

Read more about this [example](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-anonymous) in the *AWS Identity and Access Management User Guide*.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement" : {
    "Effect" : "Deny",
    "Principal" : "*",
    "Action" : "s3:*",
    "Resource" : [ "arn:aws:s3:::BUCKETNAME/*", "arn:aws:s3:::BUCKETNAME" ],
    "Condition" : {
      "ArnNotEquals" : {
        "aws:PrincipalArn" : "arn:aws:iam::444455556666:user/user-name"
      }
    }
  }
}
```

------

### Example: Allow cross-account access
<a name="iam-policy-builder-create-ex-cross-account"></a>

The following example shows how to allow another AWS account to upload objects to your bucket while retaining full owner control of the uploaded objects.

```
    public String allowCrossAccountAccessExample() {
        IamPolicy policy = IamPolicy.builder()
                .addStatement(b -> b
                        .effect(IamEffect.ALLOW)
                        .addPrincipal(IamPrincipalType.AWS, "111122223333")
                        .addAction("s3:PutObject")
                        .addResource("arn:aws:s3:::amzn-s3-demo-bucket/*")
                        .addCondition(b1 -> b1
                                .operator(IamConditionOperator.STRING_EQUALS)
                                .key("s3:x-amz-acl")
                                .value("bucket-owner-full-control")))
                .build();
        return policy.toJson(IamPolicyWriter.builder()
                .prettyPrint(true).build());
    }
```

#### JSON output
<a name="iam-policy-builder-create-ex-json-cross-account"></a>

The last statement in the previous example returns the following JSON string.

Read more about this [example](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html#example-bucket-policies-acl-2) in the *Amazon Simple Storage Service User Guide*.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement" : {
    "Effect" : "Allow",
    "Principal" : {
      "AWS" : "111122223333"
    },
    "Action" : "s3:PutObject",
    "Resource" : "arn:aws:s3:::amzn-s3-demo-bucket/*",
    "Condition" : {
      "StringEquals" : {
        "s3:x-amz-acl" : "bucket-owner-full-control"
      }
    }
  }
}
```

------

## Use an `IamPolicy` with IAM
<a name="iam-policy-builder-work-with-service"></a>

After you have created a `IamPolicy` instance, you use an [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/iam/IamClient.html](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/iam/IamClient.html) to work with the IAM service.

The following example builds a policy that allows an [IAM identity](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) to write items to a DynamoDB table in the account that is specified with the `accountID` parameter. The policy is then uploaded to IAM as a JSON string.

```
    public String createAndUploadPolicyExample(IamClient iam, String accountID, String policyName) {
        // Build the policy.
        IamPolicy policy =
                IamPolicy.builder() // 'version' defaults to "2012-10-17".
                        .addStatement(IamStatement.builder()
                                .effect(IamEffect.ALLOW)
                                .addAction("dynamodb:PutItem")
                                .addResource("arn:aws:dynamodb:us-east-1:" + accountID + ":table/exampleTableName")
                                .build())
                        .build();
        // Upload the policy.
        iam.createPolicy(r -> r.policyName(policyName).policyDocument(policy.toJson()));
        return policy.toJson(IamPolicyWriter.builder().prettyPrint(true).build());
    }
```

The next example builds on the previous example. The code downloads the policy and uses it as the basis for a new policy by copying and altering the statement. The new policy is then uploaded.

```
    public String createNewBasedOnExistingPolicyExample(IamClient iam, String accountID, String policyName, String newPolicyName) {

        String policyArn = "arn:aws:iam::" + accountID + ":policy/" + policyName;
        GetPolicyResponse getPolicyResponse = iam.getPolicy(r -> r.policyArn(policyArn));

        String policyVersion = getPolicyResponse.policy().defaultVersionId();
        GetPolicyVersionResponse getPolicyVersionResponse =
                iam.getPolicyVersion(r -> r.policyArn(policyArn).versionId(policyVersion));

        // Create an IamPolicy instance from the JSON string returned from IAM.
        String decodedPolicy = URLDecoder.decode(getPolicyVersionResponse.policyVersion().document(), StandardCharsets.UTF_8);
        IamPolicy policy = IamPolicy.fromJson(decodedPolicy);

            /*
             All IamPolicy components are immutable, so use the copy method that creates a new instance that
             can be altered in the same method call.

             Add the ability to get an item from DynamoDB as an additional action.
            */
        IamStatement newStatement = policy.statements().get(0).copy(s -> s.addAction("dynamodb:GetItem"));

        // Create a new statement that replaces the original statement.
        IamPolicy newPolicy = policy.copy(p -> p.statements(Arrays.asList(newStatement)));

        // Upload the new policy. IAM now has both policies.
        iam.createPolicy(r -> r.policyName(newPolicyName)
                .policyDocument(newPolicy.toJson()));

        return newPolicy.toJson(IamPolicyWriter.builder().prettyPrint(true).build());
    }
```

### IamClient
<a name="iam-policy-builder-work-with-serivce-create-client"></a>

The previous examples use an `IamClient` argument that is created as shown in the following snippet.

```
IamClient iam = IamClient.builder().region(Region.AWS_GLOBAL).build();
```

### Policies in JSON
<a name="iam-policy-builder-work-with-serivce-json"></a>

The examples return the following JSON strings.

```
First example
{
  "Version": "2012-10-17",
  "Statement" : {
    "Effect" : "Allow",
    "Action" : "dynamodb:PutItem",
    "Resource" : "arn:aws:dynamodb:us-east-1:{{111122223333}}:table/exampleTableName"
  }
}

Second example
{
  "Version": "2012-10-17",
  "Statement" : {
    "Effect" : "Allow",
    "Action" : [ "dynamodb:PutItem", "dynamodb:GetItem" ],
    "Resource" : "arn:aws:dynamodb:us-east-1:{{111122223333}}:table/exampleTableName"
  }
}
```
