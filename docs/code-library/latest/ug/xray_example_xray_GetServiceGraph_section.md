---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/xray_example_xray_GetServiceGraph_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetServiceGraph` with an AWS SDK or CLI
<a name="xray_example_xray_GetServiceGraph_section"></a>

The following code examples show how to use `GetServiceGraph`.

------
#### [ CLI ]

**AWS CLI**
**To get a service graph**
The following example displays a document within a specified time period that describes services processing incoming requests, and the downstream services that they call as a result.:

```
aws xray get-service-graph \
    --start-time {{1568835392.0}}
    --end-time {{1568835446.0}}
```
Output:

```
{
    "Services": [
        {
            "ReferenceId": 0,
            "Name": "Scorekeep",
            "Names": [
                "Scorekeep"
            ],
            "Root": true,
            "Type": "AWS::ElasticBeanstalk::Environment",
            "State": "active",
            "StartTime": 1568835392.0,
            "EndTime": 1568835446.0,
            "Edges": [
                {
                    "ReferenceId": 1,
                    "StartTime": 1568835392.0,
                    "EndTime": 1568835446.0,
                    "SummaryStatistics": {
                        "OkCount": 14,
                        "ErrorStatistics": {
                            "ThrottleCount": 0,
                            "OtherCount": 0,
                            "TotalCount": 0
                        },
                        "FaultStatistics": {
                            "OtherCount": 0,
                            "TotalCount": 0
                        },
                        "TotalCount": 14,
                        "TotalResponseTime": 0.13
                    },
                    "ResponseTimeHistogram": [
                        {
                            "Value": 0.008,
                            "Count": 1
                        },
                        {
                            "Value": 0.005,
                            "Count": 7
                        },
                        {
                            "Value": 0.009,
                            "Count": 1
                        },
                        {
                            "Value": 0.021,
                            "Count": 1
                        },
                        {
                            "Value": 0.038,
                            "Count": 1
                        },
                        {
                            "Value": 0.007,
                            "Count": 1
                        },
                        {
                            "Value": 0.006,
                            "Count": 2
                        }
                    ],
                    "Aliases": []
                },

                ... TRUNCATED FOR BREVITY ...

            ]
        }
    ],
    "StartTime": 1568835392.0,
    "EndTime": 1568835446.0,
    "ContainsOldGroupVersions": false
}
```
For more information, see [Using the AWS X-Ray API with the AWS CLI](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-tutorial.html) in the *AWS X-Ray Developer Guide*.
+  For API details, see [GetServiceGraph](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-service-graph.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/xray#code-examples).

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.xray.XRayClient;
import software.amazon.awssdk.services.xray.model.GetServiceGraphRequest;
import software.amazon.awssdk.services.xray.model.GetServiceGraphResponse;
import software.amazon.awssdk.services.xray.model.Service;
import software.amazon.awssdk.services.xray.model.XRayException;
import java.time.LocalDateTime;
import java.time.Instant;
import java.time.ZoneId;
import java.util.List;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class GetServiceGraph {
    public static void main(String[] args) {
        final String usage = """

                Usage:    <groupName>

                Where:
                   groupName - The name of a group based on which you want to generate a graph.

                """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String groupName = args[0];
        Region region = Region.US_EAST_1;
        XRayClient xRayClient = XRayClient.builder()
                .region(region)
                .build();
        getGraph(xRayClient, groupName);
    }

    public static void getGraph(XRayClient xRayClient, String groupName) {
        try {
            // The Instant values have to be 6 hours apart.
            LocalDateTime localDateTime = LocalDateTime.parse("2022-03-09T06:00:00");
            Instant start = localDateTime.atZone(ZoneId.of("America/New_York")).toInstant();

            LocalDateTime localDateTime2 = LocalDateTime.parse("2022-03-09T12:00:00");
            Instant end = localDateTime2.atZone(ZoneId.of("America/New_York")).toInstant();

            GetServiceGraphRequest getServiceGraphRequest = GetServiceGraphRequest.builder()
                    .groupName(groupName)
                    .startTime(start)
                    .endTime(end)
                    .build();

            GetServiceGraphResponse graphResponse = xRayClient.getServiceGraph(getServiceGraphRequest);
            List<Service> services = graphResponse.services();
            for (Service service : services) {
                System.out.println("The name of the service is  " + service.name());
            }

        } catch (XRayException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }
}
```
+  For API details, see [GetServiceGraph](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetServiceGraph) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Kotlin ]

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/xray#code-examples).

```
suspend fun getGraph(groupNameVal: String?) {
    val time = aws.smithy.kotlin.runtime.time.Instant
    val getServiceGraphRequest =
        GetServiceGraphRequest {
            groupName = groupNameVal
            this.startTime = time.now()
            endTime = time.now()
        }
    XRayClient.fromEnvironment { region = "us-east-1" }.use { xRayClient ->
        val response = xRayClient.getServiceGraph(getServiceGraphRequest)
        response.services?.forEach { service ->
            println("The name of the service is  ${service.name}")
        }
    }
}
```
+  For API details, see [GetServiceGraph](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

------
