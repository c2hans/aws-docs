---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPoliciesGrantingServiceAccess.html
---

# ListPoliciesGrantingServiceAccess
<a name="API_ListPoliciesGrantingServiceAccess"></a>

Retrieves a list of policies that the IAM identity (user, group, or role) can use to access each specified service.

**Note**
This operation does not use other policy types when determining whether a resource could access a service. These other policy types include resource-based policies, access control lists, AWS Organizations policies, IAM permissions boundaries, and AWS STS assume role policies. It only applies permissions policy logic. For more about the evaluation of policy types, see [Evaluating policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html#policy-eval-basics) in the *IAM User Guide*.

The list of policies returned by the operation depends on the ARN of the identity that you provide.
+  **User** – The list of policies includes the managed and inline policies that are attached to the user directly. The list also includes any additional managed and inline policies that are attached to the group to which the user belongs.
+  **Group** – The list of policies includes only the managed and inline policies that are attached to the group directly. Policies that are attached to the group’s user are not included.
+  **Role** – The list of policies includes only the managed and inline policies that are attached to the role.

For each managed policy, this operation returns the ARN and policy name. For each inline policy, it returns the policy name and the entity to which it is attached. Inline policies do not have an ARN. For more information about these policy types, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) in the *IAM User Guide*.

Policies that are attached to users and roles as permissions boundaries are not returned. To view which managed policy is currently used to set the permissions boundary for a user or role, use the [GetUser](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetUser.html) or [GetRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRole.html) operations.

## Request Parameters
<a name="API_ListPoliciesGrantingServiceAccess_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Arn **
The ARN of the IAM identity (user, group, or role) whose policies you want to list.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** Marker **
Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the `Marker` element in the response that you received to indicate where the next call should start.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\u0020-\u00FF]+`
Required: No

 **ServiceNamespaces.member.N**
The service namespace for the AWS services whose policies you want to list.
To learn the service namespace for a service, see [Actions, resources, and condition keys for AWS services](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html) in the *IAM User Guide*. Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, `(service prefix: a4b)`. For more information about service namespaces, see [AWS service namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces) in the * AWS General Reference*.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w-]*`
Required: Yes

## Response Elements
<a name="API_ListPoliciesGrantingServiceAccess_ResponseElements"></a>

The following elements are returned by the service.

 ** IsTruncated **
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the `Marker` request parameter to retrieve more items. We recommend that you check `IsTruncated` after every call to ensure that you receive all your results.
Type: Boolean

 ** Marker **
When `IsTruncated` is `true`, this element is present and contains the value to use for the `Marker` parameter in a subsequent pagination request.
Type: String

 **PoliciesGrantingServiceAccess.member.N**
A `ListPoliciesGrantingServiceAccess` object that contains details about the permissions policies attached to the specified identity (user, group, or role).
Type: Array of [ListPoliciesGrantingServiceAccessEntry](API_ListPoliciesGrantingServiceAccessEntry.md) objects

## Errors
<a name="API_ListPoliciesGrantingServiceAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

## Examples
<a name="API_ListPoliciesGrantingServiceAccess_Examples"></a>

### Example
<a name="API_ListPoliciesGrantingServiceAccess_Example_1"></a>

This example illustrates one usage of ListPoliciesGrantingServiceAccess.

#### Sample Request
<a name="API_ListPoliciesGrantingServiceAccess_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=ListPoliciesGrantingServiceAccess
&Arn=arn:aws:iam::123456789012:user/ExampleUser01
&ServiceNamespace.member.1=iam
&ServiceNamespace.member.2=ec2
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListPoliciesGrantingServiceAccess_Example_1_Response"></a>

```
<IsTruncated>false</IsTruncated>
<PoliciesGrantingServiceAccess>
    <member>
        <Policies>
            <member>
                <PolicyArn>arn:aws:iam::123456789012:policy/ExampleIamPolicy</PolicyArn>
                <PolicyName>ExampleIamPolicy</PolicyName>
                <PolicyType>MANAGED</PolicyType>
            </member>
            <member>
                <EntityName>AWSExampleGroup1</EntityName>
                <EntityType>GROUP</EntityType>
                <PolicyName>policygen-AWSExampleGroup1-201810241414</PolicyName>
                <PolicyType>INLINE</PolicyType>
            </member>
        </Policies>
        <ServiceNamespace>iam</ServiceNamespace>
    </member>
    <member>
        <Policies>
            <member>
                <PolicyArn>arn:aws:iam::123456789012:policy/ExampleEc2Policy</PolicyArn>
                <PolicyName>ExampleEc2Policy</PolicyName>
                <PolicyType>MANAGED</PolicyType>
            </member>
        </Policies>
        <ServiceNamespace>ec2</ServiceNamespace>
    </member>
</PoliciesGrantingServiceAccess>
```

## See Also
<a name="API_ListPoliciesGrantingServiceAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/ListPoliciesGrantingServiceAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/ListPoliciesGrantingServiceAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ListPoliciesGrantingServiceAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/ListPoliciesGrantingServiceAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ListPoliciesGrantingServiceAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/ListPoliciesGrantingServiceAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/ListPoliciesGrantingServiceAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/ListPoliciesGrantingServiceAccess)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/ListPoliciesGrantingServiceAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ListPoliciesGrantingServiceAccess)
