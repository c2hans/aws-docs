---
source_url: https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-ec2-key-pairs.html
---

The AWS SDK for Java 1.x reached end-of-support on December 31, 2025. We recommend that you migrate to the [AWS SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html) to continue receiving new features, availability improvements, and security updates.

# Working with Amazon EC2 Key Pairs
<a name="examples-ec2-key-pairs"></a>

## Creating a Key Pair
<a name="creating-a-key-pair"></a>

To create a key pair, call the AmazonEC2Client’s `createKeyPair` method with a [CreateKeyPairRequest](https://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/services/ec2/model/CreateKeyPairRequest.html) that contains the key’s name.

 **Imports**

```
import com.amazonaws.services.ec2.AmazonEC2;
import com.amazonaws.services.ec2.AmazonEC2ClientBuilder;
import com.amazonaws.services.ec2.model.CreateKeyPairRequest;
import com.amazonaws.services.ec2.model.CreateKeyPairResult;
```

 **Code**

```
final AmazonEC2 ec2 = AmazonEC2ClientBuilder.defaultClient();

CreateKeyPairRequest request = new CreateKeyPairRequest()
    .withKeyName(key_name);

CreateKeyPairResult response = ec2.createKeyPair(request);
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/java/example_code/ec2/src/main/java/aws/example/ec2/CreateKeyPair.java).

## Describing Key Pairs
<a name="describing-key-pairs"></a>

To list your key pairs or to get information about them, call the AmazonEC2Client’s `describeKeyPairs` method. It returns a [DescribeKeyPairsResult](https://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/services/ec2/model/DescribeKeyPairsResult.html) that you can use to access the list of key pairs by calling its `getKeyPairs` method, which returns a list of [KeyPairInfo](https://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/services/ec2/model/KeyPairInfo.html) objects.

 **Imports**

```
import com.amazonaws.services.ec2.AmazonEC2;
import com.amazonaws.services.ec2.AmazonEC2ClientBuilder;
import com.amazonaws.services.ec2.model.DescribeKeyPairsResult;
import com.amazonaws.services.ec2.model.KeyPairInfo;
```

 **Code**

```
final AmazonEC2 ec2 = AmazonEC2ClientBuilder.defaultClient();

DescribeKeyPairsResult response = ec2.describeKeyPairs();

for(KeyPairInfo key_pair : response.getKeyPairs()) {
    System.out.printf(
        "Found key pair with name %s " +
        "and fingerprint %s",
        key_pair.getKeyName(),
        key_pair.getKeyFingerprint());
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/java/example_code/ec2/src/main/java/aws/example/ec2/DescribeKeyPairs.java).

## Deleting a Key Pair
<a name="deleting-a-key-pair"></a>

To delete a key pair, call the AmazonEC2Client’s `deleteKeyPair` method, passing it a [DeleteKeyPairRequest](https://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/services/ec2/model/DeleteKeyPairRequest.html) that contains the name of the key pair to delete.

 **Imports**

```
import com.amazonaws.services.ec2.AmazonEC2;
import com.amazonaws.services.ec2.AmazonEC2ClientBuilder;
import com.amazonaws.services.ec2.model.DeleteKeyPairRequest;
import com.amazonaws.services.ec2.model.DeleteKeyPairResult;
```

 **Code**

```
final AmazonEC2 ec2 = AmazonEC2ClientBuilder.defaultClient();

DeleteKeyPairRequest request = new DeleteKeyPairRequest()
    .withKeyName(key_name);

DeleteKeyPairResult response = ec2.deleteKeyPair(request);
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/java/example_code/ec2/src/main/java/aws/example/ec2/DeleteKeyPair.java).

## More Information
<a name="more-information"></a>
+  [Amazon EC2 Key Pairs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in the Amazon EC2 User Guide for Linux Instances
+  [CreateKeyPair](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateKeyPair.html) in the Amazon EC2 API Reference
+  [DescribeKeyPairs](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeKeyPairs.html) in the Amazon EC2 API Reference
+  [DeleteKeyPair](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteKeyPair.html) in the Amazon EC2 API Reference

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
