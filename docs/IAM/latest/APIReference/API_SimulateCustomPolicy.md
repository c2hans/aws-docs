---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_SimulateCustomPolicy.html
---

# SimulateCustomPolicy
<a name="API_SimulateCustomPolicy"></a>

Simulate how a set of IAM policies and optionally a resource-based policy works with a list of API operations and AWS resources to determine the policies' effective permissions. The policies are provided as strings.

The simulation does not perform the API operations; it only checks the authorization to determine if the simulated policies allow or deny the operations. You can simulate resources that don't exist in your account.

If you want to simulate existing policies that are attached to an IAM user, group, or role, use [SimulatePrincipalPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SimulatePrincipalPolicy.html) instead.

Context keys are variables that are maintained by AWS and its services and which provide details about the context of an API query request. You can use the `Condition` element of an IAM policy to evaluate context keys. To get the list of context keys that the policies require for correct simulation, use [GetContextKeysForCustomPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetContextKeysForCustomPolicy.html).

If the output is long, you can use `MaxItems` and `Marker` parameters to paginate the results.

**Note**
The IAM policy simulator evaluates statements in identity-based policies, service control policies (SCPs) including their condition keys and resource scoping, and the inputs that you provide during simulation. The policy simulator results can differ from your live AWS environment. We recommend that you check your policies against your live AWS environment after testing using the policy simulator to confirm that you have the desired results. For more information about using the policy simulator, see [Testing IAM policies with the IAM policy simulator ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html)in the *IAM User Guide*.

## Request Parameters
<a name="API_SimulateCustomPolicy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **ActionNames.member.N**
A list of names of API operations to evaluate in the simulation. Each operation is evaluated against each resource. Each operation must include the service identifier, such as `iam:CreateUser`. This operation does not support using wildcards (\*) in an action name.
Type: Array of strings
Length Constraints: Minimum length of 3. Maximum length of 128.
Required: Yes

 ** CallerArn **
The ARN of the IAM user, group, or role that you want to use as the simulated caller of the API operations. `CallerArn` is required if you include a `ResourcePolicy` so that the policy's `Principal` element has a value to use in evaluating the policy.
You cannot specify the ARN of an assumed role, federated user, or a service principal.
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

 **OrderedOrganizationPolicyInputList.member.N**
An ordered list of service control policies (SCPs) to include in the simulation. Each element represents one level of an Organizations hierarchy, from the organization root to the account.
The simulator evaluates SCPs in the order that you provide, consistent with how Organizations enforces SCPs. The first element must represent the organization root, and the last element must represent the account. Any elements between them represent organizational units (OUs) in descending order.
Use this parameter to simulate the effect of an SCP hierarchy without calling [SimulatePrincipalPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SimulatePrincipalPolicy.html).
Type: Array of [OrderedOrganizationPolicyType](API_OrderedOrganizationPolicyType.md) objects
Array Members: Maximum number of 7 items.
Required: No

 **PermissionsBoundaryPolicyInputList.member.N**
The IAM permissions boundary policy to simulate. The permissions boundary sets the maximum permissions that an IAM entity can have. You can input only one permissions boundary when you pass a policy to this operation. For more information about permissions boundaries, see [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*. The policy input is specified as a string that contains the complete, valid JSON text of a permissions boundary policy.
The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see [IAM and AWS STS character quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length).
The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:
+ Any printable ASCII character ranging from the space character (`\u0020`) through the end of the ASCII character range
+ The printable characters in the Basic Latin and Latin-1 Supplement character set (through `\u00FF`)
+ The special characters tab (`\u0009`), line feed (`\u000A`), and carriage return (`\u000D`)
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

 **PolicyInputList.member.N**
A list of policy documents to include in the simulation. Each document is specified as a string containing the complete, valid JSON text of an IAM policy. Do not include any resource-based policies in this parameter. Any resource-based policy must be submitted with the `ResourcePolicy` parameter. The policies cannot be "scope-down" policies, such as you could include in a call to [GetFederationToken](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetFederationToken.html) or one of the [AssumeRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AssumeRole.html) API operations. In other words, do not use policies designed to restrict what a user can do while using the temporary credentials.
The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see [IAM and AWS STS character quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length).
The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:
+ Any printable ASCII character ranging from the space character (`\u0020`) through the end of the ASCII character range
+ The printable characters in the Basic Latin and Latin-1 Supplement character set (through `\u00FF`)
+ The special characters tab (`\u0009`), line feed (`\u000A`), and carriage return (`\u000D`)
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: Yes

 **ResourceArns.member.N**
A list of ARNs of AWS resources to include in the simulation. If this parameter is not provided, then the value defaults to `*` (all resources). Each API in the `ActionNames` parameter is evaluated for each resource in this list. The simulation determines the access result (allowed or denied) of each combination and reports it in the response. You can simulate resources that don't exist in your account.
The simulation does not automatically retrieve policies for the specified resources. If you want to include a resource policy in the simulation, then you must include the policy as a string in the `ResourcePolicy` parameter.
If you include a `ResourcePolicy`, then it must be applicable to all of the resources included in the simulation or you receive an invalid input error.
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
An ARN representing the AWS account ID that specifies the owner of any simulated resource that does not identify its owner in the resource ARN. Examples of resource ARNs include an S3 bucket or object. If `ResourceOwner` is specified, it is also used as the account owner of any `ResourcePolicy` included in the simulation. If the `ResourceOwner` parameter is not specified, then the owner of the resources and the resource policy defaults to the account of the identity provided in `CallerArn`. This parameter is required only if you specify a resource-based policy and account that owns the resource is different from the account that owns the simulated calling user `CallerArn`.
The ARN for an account uses the following syntax: `arn:aws:iam::AWS-account-ID:root`. For example, to represent the account with the 112233445566 ID, use the following ARN: `arn:aws:iam::112233445566-ID:root`.
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
<a name="API_SimulateCustomPolicy_ResponseElements"></a>

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
<a name="API_SimulateCustomPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** PolicyEvaluation **
The request failed because a provided policy could not be successfully evaluated. An additional detailed message indicates the source of the failure.
HTTP Status Code: 500

## Examples
<a name="API_SimulateCustomPolicy_Examples"></a>

### Example: Using Context Keys in a Policy Simulation
<a name="API_SimulateCustomPolicy_Example_1"></a>

This example specifies a policy by string and supplies a `ContextEntry` to use for the context key that the policy references. Note that all parameters are shown in unencoded form here for clarity but must be URL encoded to be included as a part of a real HTML request. The results show that the policy allows `s3:ListBucket` access to the S3 bucket named `teambucket`.

#### Sample Request
<a name="API_SimulateCustomPolicy_Example_1_Request"></a>

```
https://iam.amazonaws.com/Action=SimulateCustomPolicy
&ActionNames.member.1=s3:ListBucket
&ResourceArns.member.1=arn:aws:s3:::teambucket
&ContextEntries.member.1.ContextKeyName=aws:MultiFactorAuthPresent
&ContextEntries.member.1.ContextKeyType=boolean
&ContextEntries.member.1.ContextKeyValues.member.1=true
&PermissionsBoundaryPolicyInputList.member.1='{
  "Version":"2012-10-17",
  "Statement":{
    "Effect":"Deny",
    "Action":{"iam:GetRole","iam:CreateRole","iam:DeleteRole"},
    "Resource":{"*"}
    }
}'
&PolicyInputList.member.1='{
  "Version":"2012-10-17",
  "Statement":{
    "Effect":"Allow",
    "Action":"s3:ListBucket",
    "Resource":"arn:aws:s3:::teambucket",
    "Condition":{
      "Bool":{"aws:MultiFactorAuthPresent":"true"}
    }
  }
}'
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_SimulateCustomPolicy_Example_1_Response"></a>

```
<SimulateCustomPolicyResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <SimulateCustomPolicyResult>
    <IsTruncated>false</IsTruncated>
    <EvaluationResults>
      <member>
        <MatchedStatements>
          <member>
            <SourcePolicyId>PolicyInputList.1</SourcePolicyId>
            <EndPosition>
              <Column>4</Column>
              <Line>11</Line>
            </EndPosition>
            <StartPosition>
              <Column>16</Column>
              <Line>4</Line>
            </StartPosition>
          </member>
        </MatchedStatements>
        <MissingContextValues/>
        <EvalResourceName>arn:aws:s3:::teambucket</EvalResourceName>
        <EvalDecision>allowed</EvalDecision>
        <EvalActionName>s3:ListBucket</EvalActionName>
      </member>
    </EvaluationResults>
  </SimulateCustomPolicyResult>
  <ResponseMetadata>
    <RequestId>1cdb5b0a-4c15-11e5-b121-bd8c7EXAMPLE</RequestId>
  </ResponseMetadata>
</SimulateCustomPolicyResponse>
```

### Example: Same-Account Simulation
<a name="API_SimulateCustomPolicy_Example_2"></a>

This example specifies an identity-based policy and a permissions boundary for the user Mateo. Both policies allow IAM actions only. However, a resource-based policy permits Mateo to perform the actions `s3:Put*` or `s3:List*` on the Production bucket. As a result, the simulation allows the action. Note that for same-account simulations where a resource ARN is specified, the `EvalDecisionDetails` parameter is returned, but the response is empty.

#### Sample Request
<a name="API_SimulateCustomPolicy_Example_2_Request"></a>

```
https://iam.amazonaws.com/Action=SimulateCustomPolicy
&ActionNames.member.1=s3:PutObject
&CallerArn:arn:aws:iam::111122223333:user/mateo
&ResourceArns.member.1=arn:aws:s3:::production/Test
&ResourceOwner=arn:aws:iam::111122223333:root
&PermissionsBoundaryPolicyInputList.member.1='{
  "Version":"2012-10-17",
  "Statement":{
    "Effect":"Allow",
    "Action":{"iam:*"},
    "Resource":{"*"}
 }
}'
&PolicyInputList.member.1='{
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
    "Principal":{"AWS":"arn:aws:iam::111122223333:user/mateo"}
    "Action":{"s3:List*","s3:Put*"},
    "Resource":{"arn:aws:s3:::production/*"}
 }
}'
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_SimulateCustomPolicy_Example_2_Response"></a>

```
<SimulateCustomPolicyResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
    <SimulateCustomPolicyResult>
        <IsTruncated>false</IsTruncated>
        <EvaluationResults>
            <member>
                <EvalDecisionDetails/>
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
                <MissingContextValues/>
                <EvalResourceName>arn:aws:s3:::production/Test</EvalResourceName>
                <EvalDecision>allowed</EvalDecision>
                <EvalActionName>s3:PutObject</EvalActionName>
                <ResourceSpecificResults>
                    <member>
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
                        <EvalResourceDecision>allowed</EvalResourceDecision>
                        <MissingContextValues/>
                        <EvalResourceName>arn:aws:s3:::production/Test</EvalResourceName>
                    </member>
                </ResourceSpecificResults>
            </member>
        </EvaluationResults>
    </SimulateCustomPolicyResult>
    <ResponseMetadata>
        <RequestId>7b2092ca-5d35-499d-bc6d-e9b49EXAMPLE</RequestId>
    </ResponseMetadata>
</SimulateCustomPolicyResponse>
```

## See Also
<a name="API_SimulateCustomPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/SimulateCustomPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/SimulateCustomPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/SimulateCustomPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/SimulateCustomPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/SimulateCustomPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/SimulateCustomPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/SimulateCustomPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/SimulateCustomPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/SimulateCustomPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/SimulateCustomPolicy)
