---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_Options.html
---

# Options
<a name="API_Options"></a>

The options you can specify when you create a grant or a new version of a grant, such as activation override behavior. For more information, see [Granted licenses in License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/granted-licenses.html) in the * AWS License Manager User Guide*.

## Contents
<a name="API_Options_Contents"></a>

 ** ActivationOverrideBehavior **   <a name="licensemanager-Type-Options-ActivationOverrideBehavior"></a>
An activation option for your grant that determines the behavior of activating a grant. Activation options can only be used with granted licenses sourced from the AWS Marketplace. Additionally, the operation must activate the grant. For the `CreateGrantVersion` operation, specify `ACTIVE` for the `Status` parameter. For the `CreateGrant` operation, specify `ACTIVE` for the `DesiredStatus` option.
+ As a license administrator, you can optionally specify an `ActivationOverrideBehavior` when activating a grant.
+ As a grantor, you can optionally specify an `ActivationOverrideBehavior` when you activate a grant for a grantee account in your organization.
+ As a grantee, if the grantor creating the distributed grant doesn’t specify an `ActivationOverrideBehavior`, you can optionally specify one when you are activating the grant.
DISTRIBUTED\_GRANTS\_ONLY
Use this value to activate a grant without replacing any member account’s active grants for the same product.
ALL\_GRANTS\_PERMITTED\_BY\_ISSUER
Use this value to activate a grant and disable other active grants in any member accounts for the same product. This action will also replace their previously activated grants with this activated grant.
Type: String
Valid Values: `DISTRIBUTED_GRANTS_ONLY | ALL_GRANTS_PERMITTED_BY_ISSUER`
Required: No

 ** DesiredStatus **   <a name="licensemanager-Type-Options-DesiredStatus"></a>
The status of the grant after License Manager creates it. The only supported value is `ACTIVE`. Specify `ACTIVE` to create and activate the grant in one request.
You can specify this option only for the `CreateGrant` operation, and only when the grant principal is an organization or an organizational unit (OU). To change the status of an existing grant, use the `Status` parameter of the `CreateGrantVersion` operation.
Type: String
Valid Values: `PENDING_WORKFLOW | PENDING_ACCEPT | REJECTED | ACTIVE | FAILED_WORKFLOW | DELETED | PENDING_DELETE | DISABLED | WORKFLOW_COMPLETED`
Required: No

## See Also
<a name="API_Options_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/Options)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/Options)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/Options)
