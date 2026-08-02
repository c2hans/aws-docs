---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchPermission.html
---

# LaunchPermission
<a name="API_LaunchPermission"></a>

Describes a launch permission.

## Contents
<a name="API_LaunchPermission_Contents"></a>

 ** Group ** (request), ** group ** (response)
The name of the group.
Type: String
Valid Values: `all`
Required: No

 ** OrganizationalUnitArn ** (request), ** organizationalUnitArn ** (response)
The Amazon Resource Name (ARN) of an organizational unit (OU).
Type: String
Required: No

 ** OrganizationArn ** (request), ** organizationArn ** (response)
The Amazon Resource Name (ARN) of an organization.
Type: String
Required: No

 ** UserId ** (request), ** userId ** (response)
The AWS account ID.
Constraints: Up to 10 000 account IDs can be specified in a single request.
Type: String
Required: No

## See Also
<a name="API_LaunchPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchPermission)
