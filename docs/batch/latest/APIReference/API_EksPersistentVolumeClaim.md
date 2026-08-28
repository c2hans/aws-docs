---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_EksPersistentVolumeClaim.html
---

# EksPersistentVolumeClaim
<a name="API_EksPersistentVolumeClaim"></a>

A `persistentVolumeClaim` volume is used to mount a [PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) into a Pod. PersistentVolumeClaims are a way for users to "claim" durable storage without knowing the details of the particular cloud environment. See the information about [PersistentVolumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) in the *Kubernetes documentation*.

## Contents
<a name="API_EksPersistentVolumeClaim_Contents"></a>

 ** claimName **   <a name="Batch-Type-EksPersistentVolumeClaim-claimName"></a>
The name of the `persistentVolumeClaim` bounded to a `persistentVolume`. For more information, see [ Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) in the *Kubernetes documentation*.
Type: String
Required: Yes

 ** readOnly **   <a name="Batch-Type-EksPersistentVolumeClaim-readOnly"></a>
An optional boolean value indicating if the mount is read only. Default is false. For more information, see [ Read Only Mounts](https://kubernetes.io/docs/concepts/storage/volumes/#read-only-mounts) in the *Kubernetes documentation*.
Type: Boolean
Required: No

## See Also
<a name="API_EksPersistentVolumeClaim_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksPersistentVolumeClaim)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksPersistentVolumeClaim)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksPersistentVolumeClaim)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
