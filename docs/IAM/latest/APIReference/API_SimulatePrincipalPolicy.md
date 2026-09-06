---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_SimulatePrincipalPolicy.html
---

# SimulatePrincipalPolicy
<a name="API_SimulatePrincipalPolicy"></a>

Simulate how a set of IAM policies attached to an IAM entity works with a list of API operations and AWS resources to determine the policies' effective permissions. The entity can be an IAM user, group, or role. If you specify a user, then the simulation also includes all of the policies that are attached to groups that the user belongs to. You can simulate resources that don't exist in your account.

You can optionally include a list of one or more additional policies specified as strings to include in the simulation. If you want to simulate only policies specified as strings, use [SimulateCustomPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SimulateCustomPolicy.html) instead.

You can also optionally include one resource-based policy to be evaluated with each of the resources included in the simulation for IAM users only.

The simulation does not perform the API operations; it only checks the authorization to determine if the simulated policies allow or deny the operations.

For cross-account simulations, `EvalDecisionDetails` returns the decision for each policy type (identity-based policy, resource-based policy, and permissions boundary). This helps you identify which policy type is responsible for an allow or deny decision when policies span multiple accounts.

 **Note:** This operation discloses information about the permissions granted to other users. If you do not want users to see other user's permissions, then consider allowing them to use [SimulateCustomPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SimulateCustomPolicy.html) instead.

Context keys are variables maintained by AWS and its services that provide details about the context of an API query request. You can use the `Condition` element of an IAM policy to evaluate context keys. To get the list of context keys that the policies require for correct simulation, use [GetContextKeysForPrincipalPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetContextKeysForPrincipalPolicy.html).

If the output is long, you can use the `MaxItems` and `Marker` parameters to paginate the results.

**Note**
The IAM policy simulator evaluates statements in identity-based policies, service control policies (SCPs) including their condition keys and resource scoping, and the inputs that you provide during simulation. The policy simulator results can differ from your live AWS environment. We recommend that you check your policies against your live AWS environment after testing using the policy simulator to confirm that you have the desired results. For more information about using the policy simulator, see [Testing IAM policies with the IAM policy simulator ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html)in the *IAM User Guide*.

## Request Parameters
<a name="API_SimulatePrincipalPolicy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **ActionNames.member.N**
A list of names of API operations to evaluate in the simulation. Each operation is evaluated for each resource. Each operation must include the service identifier, such as `iam:CreateUser`.
Type: Array of strings
Length Constraints: Minimum length of 3. Maximum length of 128.
Required: Yes

 ** CallerArn **
The ARN of the IAM user, group, or role that you want to specify as the simulated caller of the API operations. If you do not specify a `CallerArn`, it defaults to the ARN of the user, group, or role that you specify in `PolicySourceArn`. If you include both a `PolicySourceArn` (for example, `arn:aws:iam::123456789012:user/David`) and a `CallerArn` (for example, `arn:aws:iam::123456789012:user/Bob`), the result is that you simulate calling the API operations as Bob, as if Bob had David's policies.
You can specify the ARN of an IAM user, group, or role. You cannot specify the ARN of an assumed role, federated user, or a service principal.
 `CallerArn` is required if you include a `ResourcePolicy` and the `PolicySourceArn` is not the ARN for an IAM user, group, or role. This is required so that the resource-based policy's `Principal` element has a value to use in evaluating the policy.
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 **ContextEntries.member.N**
A list of context keys and corresponding values for the simulation to use. Whenever a context key is evaluated in one of the simulated IAM permissions policies, the corresponding value is supplied.
Type: Array of [ContextEntry](API_ContextEntry.md) objects
Required: No

 ** Marker **
Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the `Marker` element in the response that you received to indicate where the next call should start.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** MaxItems **
Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the `IsTruncated` response element is `true`.
If you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the `IsTruncated` response element returns `true`, and `Marker` contains a value to include in the subsequent call that tells the service where to continue from.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 **PermissionsBoundaryPolicyInputList.member.N**
The IAM permissions boundary policy to simulate. The permissions boundary sets the maximum permissions that the entity can have. You can input only one permissions boundary when you pass a policy to this operation. An IAM entity can only have one permissions boundary in effect at a time. For example, if a permissions boundary is attached to an entity and you pass in a different permissions boundary policy using this parameter, then the new permissions boundary policy is used for the simulation. For more information about permissions boundaries, see [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*. The policy input is specified as a string containing the complete, valid JSON text of a permissions boundary policy.
The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see [IAM and AWS STS character quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length).
The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:
+ Any printable ASCII character ranging from the space character (`\u0020`) through the end of the ASCII character range
+ The printable characters in the Basic Latin and Latin-1 Supplement character set (through `\u00FF`)
+ The special characters tab (`\u0009`), line feed (`\u000A`), and carriage return (`\u000D`)
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

 **PolicyExclusionList.member.N**
A list of policies to exclude from the simulation. Use this parameter to test what the simulation result would be if a policy were removed, without changing which policies are actually attached to the principal identified by `PolicySourceArn`.
Each entry is a [PolicyIdentifier](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PolicyIdentifier.html) that identifies one or more policies to exclude by policy type, by Amazon Resource Name (ARN), or by the name of an inline policy and the entity it is attached to.
Syntactically invalid identifiers, such as malformed ARNs or wildcards in disallowed positions, cause the request to fail with an `InvalidInput` error. Syntactically valid identifiers that don't match any attached policy are ignored. Resource control policies (RCPs) are not supported in this release; identifiers that target RCPs are also ignored.
Type: Array of [PolicyIdentifier](API_PolicyIdentifier.md) objects
Array Members: Maximum number of 256 items.
Required: No

 **PolicyInputList.member.N**
An optional list of additional policy documents to include in the simulation. Each document is specified as a string containing the complete, valid JSON text of an IAM policy.
The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:
+ Any printable ASCII character ranging from the space character (`\u0020`) through the end of the ASCII character range
+ The printable characters in the Basic Latin and Latin-1 Supplement character set (through `\u00FF`)
+ The special characters tab (`\u0009`), line feed (`\u000A`), and carriage return (`\u000D`)
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

 ** PolicySourceArn **
The Amazon Resource Name (ARN) of a user, group, or role whose policies you want to include in the simulation. If you specify a user, group, or role, the simulation includes all policies that are associated with that entity. If you specify a user, the simulation also includes all policies that are attached to any groups the user belongs to.
The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see [IAM and AWS STS character quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length).
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 **ResourceArns.member.N**
A list of ARNs of AWS resources to include in the simulation. If this parameter is not provided, then the value defaults to `*` (all resources). Each API in the `ActionNames` parameter is evaluated for each resource in this list. The simulation determines the access result (allowed or denied) of each combination and reports it in the response. You can simulate resources that don't exist in your account.
The simulation does not automatically retrieve policies for the specified resources. If you want to include a resource policy in the simulation, then you must include the policy as a string in the `ResourcePolicy` parameter.
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Simulation of resource-based policies isn't supported for IAM roles.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** ResourceHandlingOption **
Specifies the type of simulation to run. Different API operations that support resource-based policies require different combinations of resources. By specifying the type of simulation to run, you enable the policy simulator to enforce the presence of the required resources to ensure reliable simulation results. If your simulation does not match one of the following scenarios, then you can omit this parameter. The following list shows each of the supported scenario values and the resources that you must define to run the simulation.
Each of the Amazon EC2 scenarios requires that you specify instance, image, and security group resources. If your scenario includes an EBS volume, then you must specify that volume as a resource. If the Amazon EC2 scenario includes VPC, then you must supply the network interface resource. If it includes an IP subnet, then you must specify the subnet resource. For more information on the Amazon EC2 scenario options, see [Supported platforms](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html) in the *Amazon EC2 User Guide*.
+  **EC2-VPC-InstanceStore**

  instance, image, security group, network interface
+  **EC2-VPC-InstanceStore-Subnet**

  instance, image, security group, network interface, subnet
+  **EC2-VPC-EBS**

  instance, image, security group, network interface, volume
+  **EC2-VPC-EBS-Subnet**

  instance, image, security group, network interface, subnet, volume
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ResourceOwner **
An AWS account ID that specifies the owner of any simulated resource that does not identify its owner in the resource ARN. Examples of resource ARNs include an S3 bucket or object. If `ResourceOwner` is specified, it is also used as the account owner of any `ResourcePolicy` included in the simulation. If the `ResourceOwner` parameter is not specified, then the owner of the resources and the resource policy defaults to the account of the identity provided in `CallerArn`. This parameter is required only if you specify a resource-based policy and account that owns the resource is different from the account that owns the simulated calling user `CallerArn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** ResourcePolicy **
A resource-based policy to include in the simulation provided as a string. Each resource in the simulation is treated as if it had this policy attached. You can include only one resource-based policy in a simulation.
The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see [IAM and AWS STS character quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length).
The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:
+ Any printable ASCII character ranging from the space character (`\u0020`) through the end of the ASCII character range
+ The printable characters in the Basic Latin and Latin-1 Supplement character set (through `\u00FF`)
+ The special characters tab (`\u0009`), line feed (`\u000A`), and carriage return (`\u000D`)
Simulation of resource-based policies isn't supported for IAM roles.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

## Response Elements
<a name="API_SimulatePrincipalPolicy_ResponseElements"></a>

The following elements are returned by the service.

 **EvaluationResults.member.N**
The results of the simulation.
Type: Array of [EvaluationResult](API_EvaluationResult.md) objects

 ** IsTruncated **
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the `Marker` request parameter to retrieve more items. Note that IAM might return fewer than the `MaxItems` number of results even when there are more results available. We recommend that you check `IsTruncated` after every call to ensure that you receive all your results.
Type: Boolean

 ** Marker **
When `IsTruncated` is `true`, this element is present and contains the value to use for the `Marker` parameter in a subsequent pagination request.
Type: String

## Errors
<a name="API_SimulatePrincipalPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** PolicyEvaluation **
The request failed because a provided policy could not be successfully evaluated. An additional detailed message indicates the source of the failure.
HTTP Status Code: 500

## Examples
<a name="API_SimulatePrincipalPolicy_Examples"></a>

### Example: Simulating a Policy
<a name="API_SimulatePrincipalPolicy_Example_1"></a>

This example simulates calling the Amazon S3 API operations GetObject, PutObject, and DeleteObject for a specific S3 bucket. The simulation includes all policies that are attached to the user Jill. In this example, the user Jill has only the managed policy "AmazonS3ReadOnlyAccess" attached. Note that all parameters are shown in unencoded form here for clarity but must be URL encoded to be included as a part of a real HTML request. In the results, the simulation shows that Jill can add new files to the bucket because of the additional policy specified as a string parameter. In addition, she can read from the bucket because of the managed policy attached to the user. However, she cannot delete anything from the S3 bucket because of the default `implicitDeny`.

#### Sample Request
<a name="API_SimulatePrincipalPolicy_Example_1_Request"></a>

```
https://iam.amazonaws.com/Action=SimulatePrincipalPolicy
&ActionNames.member.1=s3:PutObject
&ActionNames.member.2=s3:GetObject
&ActionNames.member.3=s3:DeleteObject
&ResourceArns.member.1="arn:aws:s3:::my-test-bucket"
&PolicySourceArn=arn:aws:iam:::user/Jill
&PolicyInputList.member.1='{
  "Version":"2012-10-17",
  "Statement":{
    "Effect":"Allow",
    "Action":"s3:PutObject",
    "Resource":"arn:aws:s3:::my-test-bucket"
  }
}'
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_SimulatePrincipalPolicy_Example_1_Response"></a>

```
<SimulatePrincipalPolicyResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <SimulatePrincipalPolicyResult>
    <IsTruncated>false</IsTruncated>
    <EvaluationResults>
      <member>
        <MatchedStatements>
          <member>
            <SourcePolicyId>PolicyInputList.1</SourcePolicyId>
            <EndPosition>
              <Column>4</Column>
              <Line>7</Line>
            </EndPosition>
            <StartPosition>
              <Column>16</Column>
              <Line>3</Line>
            </StartPosition>
          </member>
        </MatchedStatements>
        <MissingContextValues/>
        <EvalResourceName>arn:aws:s3:::my-test-bucket</EvalResourceName>
        <EvalDecision>allowed</EvalDecision>
        <EvalActionName>s3:PutObject</EvalActionName>
      </member>
      <member>
        <MatchedStatements>
          <member>
            <SourcePolicyId>AmazonS3ReadOnlyAccess</SourcePolicyId>
            <EndPosition>
              <Column>6</Column>
              <Line>11</Line>
            </EndPosition>
            <StartPosition>
              <Column>17</Column>
              <Line>3</Line>
            </StartPosition>
          </member>
        </MatchedStatements>
        <MissingContextValues/>
        <EvalResourceName>arn:aws:s3:::my-test-bucket</EvalResourceName>
        <EvalDecision>allowed</EvalDecision>
        <EvalActionName>s3:GetObject</EvalActionName>
      </member>
      <member>
        <MatchedStatements/>
        <MissingContextValues/>
        <EvalResourceName>arn:aws:s3:::my-test-bucket</EvalResourceName>
        <EvalDecision>implicitDeny</EvalDecision>
        <EvalActionName>s3:DeleteObject</EvalActionName>
      </member>
    </EvaluationResults>
  </SimulatePrincipalPolicyResult>
  <ResponseMetadata>
    <RequestId>004d7059-4c14-11e5-b121-bd8c7EXAMPLE</RequestId>
  </ResponseMetadata>
</SimulatePrincipalPolicyResponse>
```

### Example: Same-Account Simulation
<a name="API_SimulatePrincipalPolicy_Example_2"></a>

This example evaluates policies in the same account only. The simulated user Mateo has an identity-based policy attached that allows the `iam:GetRole` action. The permissions boundary policy specified in the simulation allows all IAM and S3 actions. Note that for same-account simulations where a resource ARN is specified, the `EvalDecisionDetails` parameter is returned, but the response is empty.

#### Sample Request
<a name="API_SimulatePrincipalPolicy_Example_2_Request"></a>

```
https://iam.amazonaws.com/Action=SimulatePrincipalPolicy
&ActionNames.member.1=iam:GetRole
&ResourceArns.member.1="arn:aws:iam::111122223333:role/pol-sim-test"
&PolicySourceArn=arn:aws:iam::111122223333:user/mateo
&PermissionsBoundaryPolicyInputList.member.1='{
  "Version":"2012-10-17",
  "Statement":{
    "Effect":"Allow",
    "Action":{"iam:*","s3:*"},
    "Resource":{"*"}
  }
}'
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_SimulatePrincipalPolicy_Example_2_Response"></a>

```
<SimulatePrincipalPolicyResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
    <SimulatePrincipalPolicyResult>
        <IsTruncated>false</IsTruncated>
        <EvaluationResults>
            <member>
                <EvalDecisionDetails/>
                <PermissionsBoundaryDecisionDetail>
                    <AllowedByPermissionsBoundary>true</AllowedByPermissionsBoundary>
                </PermissionsBoundaryDecisionDetail>
                <MatchedStatements>
                    <member>
                        <SourcePolicyId>user_admin_AdminUser</SourcePolicyId>
                        <EndPosition>
                            <Column>84</Column>
                            <Line>1</Line>
                        </EndPosition>
                        <SourcePolicyType>IAM Policy</SourcePolicyType>
                        <StartPosition>
                            <Column>38</Column>
                            <Line>1</Line>
                        </StartPosition>
                    </member>
                </MatchedStatements>
                <MissingContextValues/>
                <EvalResourceName>arn:aws:iam::111122223333:role/pol-sim-test</EvalResourceName>
                <EvalDecision>allowed</EvalDecision>
                <EvalActionName>iam:GetRole</EvalActionName>
                <ResourceSpecificResults>
                    <member>
                        <PermissionsBoundaryDecisionDetail>
                            <AllowedByPermissionsBoundary>true</AllowedByPermissionsBoundary>
                        </PermissionsBoundaryDecisionDetail>
                        <MatchedStatements>
                            <member>
                                <SourcePolicyId>user_admin_AdminUser</SourcePolicyId>
                                <EndPosition>
                                    <Column>84</Column>
                                    <Line>1</Line>
                                </EndPosition>
                                <SourcePolicyType>IAM Policy</SourcePolicyType>
                                <StartPosition>
                                    <Column>38</Column>
                                    <Line>1</Line>
                                </StartPosition>
                            </member>
                        </MatchedStatements>
                        <EvalResourceDecision>allowed</EvalResourceDecision>
                        <MissingContextValues/>
                        <EvalResourceName>arn:aws:iam::111122223333:role/pol-sim-test</EvalResourceName>
                    </member>
                </ResourceSpecificResults>
            </member>
        </EvaluationResults>
    </SimulatePrincipalPolicyResult>
    <ResponseMetadata>
        <RequestId>896e97bd-ff20-47d0-9f91-5d696EXAMPLE</RequestId>
    </ResponseMetadata>
</SimulatePrincipalPolicyResponse>
```

### Example: Cross-Account Simulation
<a name="API_SimulatePrincipalPolicy_Example_3"></a>

This example is for a simulation that evaluates policies in two accounts. The resource-based policy allows the `s3:PutObject` action for the user Arnav on Mary's bucket in Account 2. However, the overall result of the simulation for the action is implicitly denied. Arnav's identity-based policy in Account 1 does not allow the action. Additionally, the permissions boundary set for Arnav in Account 1 does not allow S3 actions. The results of each of the policy types included in the simulation is returned in the `EvalDecisionDetails` parameter.

#### Sample Request
<a name="API_SimulatePrincipalPolicy_Example_3_Request"></a>

```
https://iam.amazonaws.com/Action=SimulatePrincipalPolicy
&ActionNames.member.1=s3:PutObject
&ResourceArns.member.1="arn:aws:s3:::mary/Test"
&ResourceOwner=arn:aws:iam::123456789012:root
&PolicySourceArn=arn:aws:iam::444455556666:user/arnav
&PermissionsBoundaryPolicyInputList.member.1='{
  "Version":"2012-10-17",
  "Statement":{
    "Effect":"Allow",
    "Action":{"iam:*"},
    "Resource":{"*"}
 }
}'
&ResourcePolicy='{
  "Version":"2012-10-17",
  "Statement":{
    "Effect":"Allow",
    "Principal":{"AWS":"arn:aws:iam::444455556666:user/arnav"}
    "Action":{"s3:List*","s3:Put*"},
    "Resource":{"arn:aws:s3:::mary/*"}
 }
}'
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_SimulatePrincipalPolicy_Example_3_Response"></a>

```
SimulatePrincipalPolicyResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
    <SimulatePrincipalPolicyResult>
        <IsTruncated>false</IsTruncated>
        <EvaluationResults>
            <member>
                <EvalDecisionDetails>
                    <entry>
                        <key>IAM Policy</key>
                        <value>implicitDeny</value>
                    </entry>
                    <entry>
                        <key>Resource Policy</key>
                        <value>allowed</value>
                    </entry>
                    <entry>
                        <key>Permissions Boundary Policy</key>
                        <value>implicitDeny</value>
                    </entry>
                </EvalDecisionDetails>
                <PermissionsBoundaryDecisionDetail>
                    <AllowedByPermissionsBoundary>false</AllowedByPermissionsBoundary>
                </PermissionsBoundaryDecisionDetail>
                <MatchedStatements/>
                <MissingContextValues/>
                <EvalResourceName>arn:aws:s3:::mary/Test</EvalResourceName>
                <EvalDecision>implicitDeny</EvalDecision>
                <EvalActionName>s3:PutObject</EvalActionName>
                <ResourceSpecificResults>
                    <member>
                        <EvalDecisionDetails>
                            <entry>
                                <key>Permissions Boundary Policy</key>
                                <value>implicitDeny</value>
                            </entry>
                            <entry>
                                <key>IAM Policy</key>
                                <value>implicitDeny</value>
                            </entry>
                            <entry>
                                <key>Resource Policy</key>
                                <value>allowed</value>
                            </entry>
                        </EvalDecisionDetails>
                        <PermissionsBoundaryDecisionDetail>
                            <AllowedByPermissionsBoundary>false</AllowedByPermissionsBoundary>
                        </PermissionsBoundaryDecisionDetail>
                        <MatchedStatements>
                            <member>
                                <SourcePolicyId>ResourcePolicy</SourcePolicyId>
                                <EndPosition>
                                    <Column>259</Column>
                                    <Line>1</Line>
                                </EndPosition>
                                <SourcePolicyType>Resource Policy</SourcePolicyType>
                                <StartPosition>
                                    <Column>68</Column>
                                    <Line>1</Line>
                                </StartPosition>
                            </member>
                        </MatchedStatements>
                        <EvalResourceDecision>implicitDeny</EvalResourceDecision>
                        <MissingContextValues/>
                        <EvalResourceName>arn:aws:s3:::mary/Test</EvalResourceName>
                    </member>
                </ResourceSpecificResults>
            </member>
        </EvaluationResults>
    </SimulatePrincipalPolicyResult>
    <ResponseMetadata>
        <RequestId>3ebb073c-781a-437e-81a9-2a88eEXAMPLE</RequestId>
    </ResponseMetadata>
</SimulatePrincipalPolicyResponse>
```

## See Also
<a name="API_SimulatePrincipalPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/SimulatePrincipalPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/SimulatePrincipalPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/SimulatePrincipalPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/SimulatePrincipalPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/SimulatePrincipalPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/SimulatePrincipalPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/SimulatePrincipalPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/SimulatePrincipalPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/SimulatePrincipalPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/SimulatePrincipalPolicy)
