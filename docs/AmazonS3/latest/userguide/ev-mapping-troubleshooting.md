---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/ev-mapping-troubleshooting.html
---

# Amazon EventBridge mapping and troubleshooting
<a name="ev-mapping-troubleshooting"></a>

The following table describes how Amazon S3 event types are mapped to Amazon EventBridge event types.

|  S3 event type |  Amazon EventBridge detail type  |
| --- | --- |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)<br />[https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPOST.html](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPOST.html)<br />[https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html)<br />[https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html) | Object Created |
| ObjectRemoved:Delete<br />ObjectRemoved:DeleteMarkerCreated<br />LifecycleExpiration:Delete<br />LifecycleExpiration:DeleteMarkerCreated | Object Deleted |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html) | Object Restore Initiated |
| ObjectRestore:Completed | Object Restore Completed |
| ObjectRestore:Delete | Object Restore Expired |
| LifecycleTransition | Object Storage Class Changed |
| IntelligentTiering | Object Access Tier Changed |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html) | Object Tags Added |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html) | Object Tags Deleted |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html) | Object ACL Updated |
| ObjectAnnotation:Put | Object Annotation Created |
| ObjectAnnotation:Delete | Object Annotation Removed |

## Amazon EventBridge troubleshooting
<a name="ev-troubleshooting"></a>

For information about how to troubleshoot EventBridge, see [Troubleshooting Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-troubleshooting.html) in the *Amazon EventBridge User Guide*.
