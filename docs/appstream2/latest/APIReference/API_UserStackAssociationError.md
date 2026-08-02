---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UserStackAssociationError.html
---

# UserStackAssociationError
<a name="API_UserStackAssociationError"></a>

Describes the error that is returned when a user can’t be associated with or disassociated from a stack.

## Contents
<a name="API_UserStackAssociationError_Contents"></a>

 ** ErrorCode **   <a name="WorkSpacesApplications-Type-UserStackAssociationError-ErrorCode"></a>
The error code for the error that is returned when a user can’t be associated with or disassociated from a stack.
Type: String
Valid Values: `STACK_NOT_FOUND | USER_NAME_NOT_FOUND | DIRECTORY_NOT_FOUND | INTERNAL_ERROR`
Required: No

 ** ErrorMessage **   <a name="WorkSpacesApplications-Type-UserStackAssociationError-ErrorMessage"></a>
The error message for the error that is returned when a user can’t be associated with or disassociated from a stack.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** UserStackAssociation **   <a name="WorkSpacesApplications-Type-UserStackAssociationError-UserStackAssociation"></a>
Information about the user and associated stack.
Type: [UserStackAssociation](API_UserStackAssociation.md) object
Required: No

## See Also
<a name="API_UserStackAssociationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/UserStackAssociationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/UserStackAssociationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/UserStackAssociationError)
