---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_Image.html
---

# Image
<a name="API_Image"></a>

Describes an image.

## Contents
<a name="API_Image_Contents"></a>

 ** Name **   <a name="WorkSpacesApplications-Type-Image-Name"></a>
The name of the image.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** Applications **   <a name="WorkSpacesApplications-Type-Image-Applications"></a>
The applications associated with the image.
Type: Array of [Application](API_Application.md) objects
Required: No

 ** AppstreamAgentVersion **   <a name="WorkSpacesApplications-Type-Image-AppstreamAgentVersion"></a>
The version of the WorkSpaces Applications agent to use for instances that are launched from this image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Arn **   <a name="WorkSpacesApplications-Type-Image-Arn"></a>
The ARN of the image.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** BaseImageArn **   <a name="WorkSpacesApplications-Type-Image-BaseImageArn"></a>
The ARN of the image from which this image was created.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** CreatedTime **   <a name="WorkSpacesApplications-Type-Image-CreatedTime"></a>
The time the image was created.
Type: Timestamp
Required: No

 ** Description **   <a name="WorkSpacesApplications-Type-Image-Description"></a>
The description to display.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** DisplayName **   <a name="WorkSpacesApplications-Type-Image-DisplayName"></a>
The image name to display.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** DynamicAppProvidersEnabled **   <a name="WorkSpacesApplications-Type-Image-DynamicAppProvidersEnabled"></a>
Indicates whether dynamic app providers are enabled within an WorkSpaces Applications image or not.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** ImageBuilderName **   <a name="WorkSpacesApplications-Type-Image-ImageBuilderName"></a>
The name of the image builder that was used to create the private image. If the image is shared, copied, or updated by using Managed Image Updates, this value is null.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** ImageBuilderSupported **   <a name="WorkSpacesApplications-Type-Image-ImageBuilderSupported"></a>
Indicates whether an image builder can be launched from this image.
Type: Boolean
Required: No

 ** ImageErrors **   <a name="WorkSpacesApplications-Type-Image-ImageErrors"></a>
Describes the errors that are returned when a new image can't be created.
Type: Array of [ResourceError](API_ResourceError.md) objects
Required: No

 ** ImagePermissions **   <a name="WorkSpacesApplications-Type-Image-ImagePermissions"></a>
The permissions to provide to the destination AWS account for the specified image.
Type: [ImagePermissions](API_ImagePermissions.md) object
Required: No

 ** ImageSharedWithOthers **   <a name="WorkSpacesApplications-Type-Image-ImageSharedWithOthers"></a>
Indicates whether the image is shared with another account ID.
Type: String
Valid Values: `TRUE | FALSE`
Required: No

 ** ImageType **   <a name="WorkSpacesApplications-Type-Image-ImageType"></a>
The type of the image. Images created through AMI import have type "custom", while WorkSpaces Applications provided images have type "native". Custom images support additional instance types including GeneralPurpose, MemoryOptimized, ComputeOptimized, and Accelerated instance families.
Type: String
Valid Values: `CUSTOM | NATIVE | BYOL`
Required: No

 ** LatestAppstreamAgentVersion **   <a name="WorkSpacesApplications-Type-Image-LatestAppstreamAgentVersion"></a>
Indicates whether the image is using the latest WorkSpaces Applications agent version or not.
Type: String
Valid Values: `TRUE | FALSE`
Required: No

 ** ManagedSoftwareIncluded **   <a name="WorkSpacesApplications-Type-Image-ManagedSoftwareIncluded"></a>
Indicates whether the image includes license-included applications.
Type: Boolean
Required: No

 ** Platform **   <a name="WorkSpacesApplications-Type-Image-Platform"></a>
The operating system platform of the image.
Type: String
Valid Values: `WINDOWS | WINDOWS_SERVER_2016 | WINDOWS_SERVER_2019 | WINDOWS_SERVER_2022 | WINDOWS_SERVER_2025 | WINDOWS_11 | AMAZON_LINUX2 | RHEL8 | ROCKY_LINUX8 | UBUNTU_PRO_2404`
Required: No

 ** PublicBaseImageReleasedDate **   <a name="WorkSpacesApplications-Type-Image-PublicBaseImageReleasedDate"></a>
The release date of the public base image. For private images, this date is the release date of the base image from which the image was created.
Type: Timestamp
Required: No

 ** State **   <a name="WorkSpacesApplications-Type-Image-State"></a>
The image starts in the `PENDING` state. If image creation succeeds, the state is `AVAILABLE`. If image creation fails, the state is `FAILED`.
Type: String
Valid Values: `PENDING | AVAILABLE | FAILED | COPYING | DELETING | CREATING | IMPORTING | VALIDATING`
Required: No

 ** StateChangeReason **   <a name="WorkSpacesApplications-Type-Image-StateChangeReason"></a>
The reason why the last state change occurred.
Type: [ImageStateChangeReason](API_ImageStateChangeReason.md) object
Required: No

 ** SupportedInstanceFamilies **   <a name="WorkSpacesApplications-Type-Image-SupportedInstanceFamilies"></a>
The supported instances families that determine which image a customer can use when the customer launches a fleet or image builder. The following instances families are supported:
+ General Purpose
+ Compute Optimized
+ Memory Optimized
+ Graphics G4
+ Graphics G5
+ Graphics G6
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 ** Visibility **   <a name="WorkSpacesApplications-Type-Image-Visibility"></a>
Indicates whether the image is public or private.
Type: String
Valid Values: `PUBLIC | PRIVATE | SHARED`
Required: No

## See Also
<a name="API_Image_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/Image)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/Image)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/Image)
