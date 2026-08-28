---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsCongfigureS3ControlClientJava.html
---

# Configure the S3 control client for S3 on Outposts by using the SDK for Java
<a name="S3OutpostsCongfigureS3ControlClientJava"></a>

The following example configures the Amazon S3 control client for Amazon S3 on Outposts by using the AWS SDK for Java. To use this example, replace each `{{user input placeholder}}` with your own information.

```
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.s3control.AWSS3Control;
import com.amazonaws.services.s3control.AWSS3ControlClient;

public AWSS3Control createS3ControlClient() {

    String accessKey = {{AWSAccessKey}};
    String secretKey = {{SecretAccessKey}};
    BasicAWSCredentials awsCreds = new BasicAWSCredentials(accessKey, secretKey);

    return AWSS3ControlClient.builder().enableUseArnRegion()
            .withCredentials(new AWSStaticCredentialsProvider(awsCreds))
            .build();

}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
