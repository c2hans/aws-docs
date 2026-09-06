---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/mediastore_example_mediastore_DescribeContainer_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeContainer` with an AWS SDK or CLI
<a name="mediastore_example_mediastore_DescribeContainer_section"></a>

The following code examples show how to use `DescribeContainer`.

------
#### [ CLI ]

**AWS CLI**
**To view the details of a container**
The following `describe-container` example displays the details of the specified container.

```
aws mediastore describe-container \
    --container-name {{ExampleContainer}}
```
Output:

```
{
    "Container": {
        "CreationTime": 1563558086,
        "AccessLoggingEnabled": false,
        "ARN": "arn:aws:mediastore:us-west-2:111122223333:container/ExampleContainer",
        "Status": "ACTIVE",
        "Name": "ExampleContainer",
        "Endpoint": "https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com"
    }
}
```
For more information, see [Viewing the Details for a Container](https://docs.aws.amazon.com/mediastore/latest/ug/containers-view-details.html) in the *AWS Elemental MediaStore User Guide*.
+  For API details, see [DescribeContainer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/describe-container.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/mediastore#code-examples).

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.mediastore.MediaStoreClient;
import software.amazon.awssdk.services.mediastore.model.DescribeContainerRequest;
import software.amazon.awssdk.services.mediastore.model.DescribeContainerResponse;
import software.amazon.awssdk.services.mediastore.model.MediaStoreException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class DescribeContainer {

    public static void main(String[] args) {
        final String usage = """

                Usage:    <containerName>

                Where:
                   containerName - The name of the container to describe.
                """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String containerName = args[0];
        Region region = Region.US_EAST_1;
        MediaStoreClient mediaStoreClient = MediaStoreClient.builder()
                .region(region)
                .build();

        System.out.println("Status is " + checkContainer(mediaStoreClient, containerName));
        mediaStoreClient.close();
    }

    public static String checkContainer(MediaStoreClient mediaStoreClient, String containerName) {
        try {
            DescribeContainerRequest describeContainerRequest = DescribeContainerRequest.builder()
                    .containerName(containerName)
                    .build();

            DescribeContainerResponse containerResponse = mediaStoreClient.describeContainer(describeContainerRequest);
            System.out.println("The container name is " + containerResponse.container().name());
            System.out.println("The container ARN is " + containerResponse.container().arn());
            return containerResponse.container().status().toString();

        } catch (MediaStoreException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        return "";
    }
}
```
+  For API details, see [DescribeContainer](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediastore-2017-09-01/DescribeContainer) in *AWS SDK for Java 2.x API Reference*.

------
