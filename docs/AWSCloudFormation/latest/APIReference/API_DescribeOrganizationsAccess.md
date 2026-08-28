---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeOrganizationsAccess.html
---

# DescribeOrganizationsAccess
<a name="API_DescribeOrganizationsAccess"></a>

Retrieves information about the account's `OrganizationAccess` status. This API can be called either by the management account or the delegated administrator by using the `CallAs` parameter. This API can also be called without the `CallAs` parameter by the management account.

## Request Parameters
<a name="API_DescribeOrganizationsAccess_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CallAs **
[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.
By default, `SELF` is specified.
+ If you are signed in to the management account, specify `SELF`.
+ If you are signed in to a delegated administrator account, specify `DELEGATED_ADMIN`.

  Your AWS account must be registered as a delegated administrator in the management account. For more information, see [Register a delegated administrator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) in the * AWS CloudFormation User Guide*.
Type: String
Valid Values: `SELF | DELEGATED_ADMIN`
Required: No

## Response Elements
<a name="API_DescribeOrganizationsAccess_ResponseElements"></a>

The following element is returned by the service.

 ** Status **
Presents the status of the `OrganizationAccess`.
Type: String
Valid Values: `ENABLED | DISABLED | DISABLED_PERMANENTLY`

## Errors
<a name="API_DescribeOrganizationsAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidOperation **
The specified operation isn't valid.
HTTP Status Code: 400

 ** OperationNotFound **
The specified ID refers to an operation that doesn't exist.
HTTP Status Code: 404

## Examples
<a name="API_DescribeOrganizationsAccess_Examples"></a>

### DescribeOrganizationsAccess
<a name="API_DescribeOrganizationsAccess_Example_1"></a>

This example illustrates one usage of DescribeOrganizationsAccess.

#### Sample Request
<a name="API_DescribeOrganizationsAccess_Example_1_Request"></a>

```
https://cloudformation.us-east-1.amazonaws.com/
    ?Action=DescribeOrganizationsAccess
```

#### Sample Response
<a name="API_DescribeOrganizationsAccess_Example_1_Response"></a>

```
<DescribeOrganizationsAccessResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <DescribeOrganizationsAccessResult>
    <Status>ENABLED</Status>
  </DescribeOrganizationsAccessResult>
  <ResponseMetadata>
    <RequestId>240f1cd7-48d6-41a6-b61b-65c7c81893e9</RequestId>
  </ResponseMetadata>
</DescribeOrganizationsAccessResponse>
```

## See Also
<a name="API_DescribeOrganizationsAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeOrganizationsAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/DescribeOrganizationsAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeOrganizationsAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeOrganizationsAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeOrganizationsAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeOrganizationsAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeOrganizationsAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeOrganizationsAccess)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeOrganizationsAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeOrganizationsAccess)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
