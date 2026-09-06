---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/disaster-recovery.html
---

# Disaster recovery
<a name="disaster-recovery"></a>

Amazon AppStream 2.0 has built in redundancy across up to three availability zones. This means that if a user has an active session in an availability zone that becomes degraded, they can simply disconnect and reconnect which will reserve them a session in a healthy availability zone assuming you have capacity. While this provides high availability within the Region, it does not provide a disaster recovery solution if the service experiences issues at a regional level.

To provide a disaster recovery plan for your WorkSpaces Applications users, you will first need to build out a WorkSpaces Applications environment in your secondary Region. From a design perspective, this environment should have redundant connections to your on-premises environment, if applicable, and should have no dependency on the primary Region. For example, if your WorkSpaces Applications fleet is domain joined, you should have additional domain controllers in the secondary Region with Sites and Services configured. From a WorkSpaces Applications perspective, this environment should consist of the same fleet and stack settings that you have in your primary Region. The fleet itself should run your same base image, which can be copied to your secondary Region via the console or programmatically. If the applications that run within your WorkSpaces Applications sessions have a backend dependency tied to your primary Region, that too should have regional redundancy to ensure the users can still access the application’s backend if the primary Region goes down. Your service level limits in your destination Region should match your primary Region.

## Identity routing
<a name="identity-routing"></a>

There are two distinct methods to providing access to applications in a DR scenario. At a high level, the two methods differ by how the users are directed to the failover Region. The first method is performed with a single WorkSpaces Applications application configuration in your IdP and the second method is having two separate application configurations.

### Method 1: Changing the relay state of your application
<a name="method-1"></a>

When users login to WorkSpaces Applications from an Identity Provider (IdP), following their authentication they are relayed to a specific URL that aligns to the Region and stack they are intended to have access to. For more information around the Relay State URL, refer to the [Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/external-identity-providers-setting-up-saml.html) Administration Guide. The administrator can configure a cross-Region stack built on the same WorkSpaces Applications image as the primary Region for users to failover to. The administrator can control this failover by simply updating the Relay State URL to point to the failover stack. For this method to operate properly, the associated IAM policies will need to reflect access to both stacks; primary and failover. For more details on how these IAM policies should be configured, see the following example policy.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "appstream:Stream",
            "Resource": [
                "arn:aws:appstream:us-east-1:190836837966:stack/StackName",
                "arn:aws:appstream:us-east-1:190836837966:stack/StackName"
            ],
            "Condition": {
                "StringEquals": {
                    "appstream:userId": "${saml:sub}"
                }
            }
        }
    ]
}
```

------

### Method 2: Configuring two WorkSpaces Applications applications within your IdP
<a name="method-2"></a>

This method requires the administrator to build out two separate applications for WorkSpaces Applications within the IdP. They then can either present both applications and let the user choose where to go, or they lock/hide an application until it’s time to failover. This method is better aligned to the use case of having global users that move around often. Those users should be streaming from the closest endpoint, therefore having both applications assigned gives them the option to choose the application that is configured for their nearest Region. This can also be automated, for more information see this [blog post](http://aws.amazon.com/blogs/desktop-and-application-streaming/optimize-user-experience-with-latency-based-routing-for-amazon-appstream-2-0/).

## Storage persistance
<a name="storage-persistance"></a>

When leveraging the included data persistence features of WorkSpaces Applications, such as [Application Persistence](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-settings-persistence.html) and [Home Folder Synchronization](https://docs.aws.amazon.com/appstream2/latest/developerguide/home-folders.html), you will need to replicate that data to your failover region. These features store the persistent data in an Amazon S3 bucket in the given WorkSpaces Applications region. To have the data persist cross region, you will need to replicate all changes on the source bucket to the failover regions WorkSpaces Applications bucket. This can be done with native Amazon S3 features, such as [Amazon S3 cross region replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-walkthrough1.html). Each users persistent data will reside under a folder of their hashed username. Since the username will be hashed the same cross region, simply replicating the data will provide data persistence in your secondary region. For more information about the Amazon S3 buckets used by WorkSpaces Applications, see this [guide](https://docs.aws.amazon.com/appstream2/latest/developerguide/home-folders.html#home-folders-s3).
