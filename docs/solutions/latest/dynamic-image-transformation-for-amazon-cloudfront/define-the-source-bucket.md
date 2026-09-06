---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/define-the-source-bucket.html
---

# Define the source bucket for the request
<a name="define-the-source-bucket"></a>

To define the bucket used when getting the image for a request, include **s3:BucketName** as a modification in your request. For example, if your source buckets were `"test-bucket-1, the-other-test-bucket"`, to indicate that `the-other-test-bucket` should be used when processing an image, enter the following:

```
https://<ApiEndpoint>/s3:the-other-test-bucket/<image.jpeg>
```

**Note**
Using the **s3:BucketName** tag requires that the bucket chosen is part of the **SourceBuckets** provided upon deployment. For information on how to change the **SourceBuckets** after deployment, see [Backward compatibility](backward-compatibility.md).
