---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/use-amazon-s3-website-hosting-to-host-without-a-single-web-server.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Use Amazon S3 website hosting to host without a single web server
<a name="use-amazon-s3-website-hosting-to-host-without-a-single-web-server"></a>

 Amazon Simple Storage Service (Amazon S3) can host static websites without a need for a web server. The website is highly performant and scalable at a [fraction of the cost of a](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) [traditional web server](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html). Amazon S3 is storage for the cloud, providing you with secure, durable, highly scalable object storage. A simple web services interface allows you to store and retrieve any amount of data from anywhere on the web. Each S3 object can be zero bytes to 5 TB in file size, and there’s no limit to the number of Amazon S3 objects you can store.

 You start by creating an Amazon S3 bucket, enabling the Amazon S3 website hosting feature, and configuring access permissions for the bucket. After you upload files, Amazon S3 takes care of serving your content to your visitors.

 Amazon S3 provides HTTP web-serving capabilities, and the content can be viewed by any browser. You must also configure [Amazon Route 53](https://aws.amazon.com/route53), a managed Domain Name System (DNS) service, to point your domain to your Amazon S3 bucket. The following figure illustrates this architecture, where `example.com` is the domain.

![A diagram depicting Amazon S3 website hosting.](http://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/images/s3-web-hosting.png)

 In this solution, there are no Windows or Linux servers to manage, and no need to provision machines, install operating systems, or fine-tune web server configurations. There’s also no need to manage storage infrastructure (such as, SAN, NAS) because Amazon S3 provides practically limitless cloud-based storage. Fewer moving parts means fewer troubleshooting headaches.

## Scalability and availability
<a name="scalability-and-availability"></a>

 Amazon S3 is inherently scalable. For popular websites, Amazon S3 scales seamlessly to serve thousands of HTTP or HTTPS requests per second without any changes to the architecture.

 In addition, by hosting with Amazon S3, the website is inherently highly available. Amazon S3 is designed for 99.999999999% durability, and carries a [service level agreement](https://aws.amazon.com/s3/sla/) (SLA) of 99.9% availability. Amazon S3 gives you access to the same highly scalable, reliable, fast, and inexpensive infrastructure that Amazon uses to run its own global network of websites. As soon as you upload files to Amazon S3, Amazon S3 automatically replicates your content across multiple data centers. Even if an entire AWS data center were to be impaired, your static website would still be running and available to your end users.

 Compare this solution with traditional non-AWS costs for implementing “active-active” hosting for important projects. Active-active, or deploying web servers in two distinct data centers, is prohibitive in terms of server costs and engineering time. As a result, traditional websites are usually hosted in a single data center, because most projects can’t justify the cost of “active-active” hosting.

## Encrypt data in transit
<a name="encrypt-data-in-transit"></a>

 We recommend you use HTTPS to serve static websites securely. HTTPS is the secure version of the HTTP protocol that browsers use when communicating with websites. In HTTPS, the communication protocol is encrypted using Transport Layer Security (TLS). TLS protocols are cryptographic protocols designed to provide privacy and data integrity between two or more communicating computer applications. HTTPS protects against man-in-the-middle (MITM) attacks. MITM attacks intercept and maliciously modify traffic.

 Historically, HTTPS was used for sites that handled financial information, such as banking and e-commerce sites. However, HTTPS is now becoming more of the norm rather than the exception. For example, the percentage of web pages loaded by Mozilla Firefox using HTTPS has [steadily increased to over 80%](https://letsencrypt.org/stats/) and other surveys indicate that [over 80% of all websites use HTTPS as the default.](https://w3techs.com/technologies/details/ce-httpsdefault)

 [AWS Certificate Manager](https://aws.amazon.com/certificate-manager) (ACM) is a service that lets you easily provision, manage, and deploy public and private Secure Sockets Layer (SSL)/TLS certificates for use with AWS services and your internal connected resources. See the [Using HTTPS with Amazon CloudFront](using-https-with-amazon-cloudfront.md) section of this document for more implementation information.

## Configuration basics
<a name="configuration-basics"></a>

 Configuration involves these steps:

1.  Open the AWS Management Console.

1.  On the Amazon S3 console, create an Amazon S3 bucket.
   +  Choose the AWS Region in which the files will be [geographically stored](https://aws.amazon.com/about-aws/global-infrastructure/). (If your high-availability requirements require that your website must remain available even in the case of a failure of an entire AWS Region, explore the [Amazon S3 Cross-Region Replication](https://docs.aws.amazon.com/AmazonS3/latest/UG/cross-region-replication.html) capability to automatically replicate your S3 data to another S3 bucket in a second AWS Region.) Select a Region based on its proximity to your visitors, proximity to your corporate data centers, and/or your regulatory or compliance requirements (for example, some countries have restrictive data residency regulations).
   +  Choose a bucket name that complies with [DNS naming conventions](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html).

      If you plan to use your own custom domain or subdomain, such as `example.com` or `www.example.com`, your bucket name must be the same as your domain or subdomain. For example, a website available at `http://www.example.com` must be in a bucket named `www.example.com`.
**Note**
 Each AWS account can have a maximum of 1000 buckets.

1.  Toggle on the [static website hosting feature](https://docs.aws.amazon.com/gettingstarted/latest/swh/website-hosting-intro.html) for the bucket. This generates an Amazon S3 website endpoint.

 You can access your Amazon S3-hosted website at the following URL:

```
      http://{{<bucket-name>}}.s3-website-{{<AWS-Region>}}.amazonaws.com
```

## Domain names
<a name="domain-names"></a>

 For small, non-public websites, the Amazon S3 website endpoint is probably adequate. You can also use internal DNS to point to this endpoint. For a public facing website, we recommend using a custom domain name instead of the provided Amazon S3 website endpoint. This way, users can see user-friendly URLs in their browsers. If you plan to use a custom domain name, your bucket name must match the domain name. For custom root domains (such as `example.com`), only Amazon Route 53 can configure a DNS record to point to the Amazon S3 hosted website.

 For non-root subdomains (such as `www.example.com`), any DNS service (including Amazon Route 53) can create a `CNAME` entry to the subdomain. See the [Amazon Simple Storage Service Developer Guide](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html) for more details on how to associate domain names with your website.

![A screenshot that shows configuring static website hosting using the Amazon S3 console.](http://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/images/configure-static.jpeg)

 The Amazon S3 website hosting configuration screen in the Amazon S3 console presents additional options to configure. Some of the key options are as follows:
+  You can configure a default page that users see if they visit the domain name directly (without specifying a specific page). (For Microsoft IIS web servers, this is equivalent to `default.html`. For Apache web servers, this is equivalent to `index.html`.)
+  You can also specify a custom 404- Page Not Found error page if the user stumbles onto a non-existent page.
+  You can enable logging to give you access to the [raw web access logs](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerLogs.html). (By default, logging is disabled.)
+  You can add tags to your Amazon S3 bucket. These tags help when you want to [analyze your AWS spend by project](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketBilling.html).

## Amazon S3 object names
<a name="amazon-s3-object-names"></a>

 In Amazon S3, a bucket is a flat container of objects. It doesn’t provide a hierarchical organization the way the file system on your computer does. However, there is a straightforward mapping between a file system’s folders/files to Amazon S3 objects. The example that follows shows how folders/files are mapped to Amazon S3 objects. Most third-party tools, as well as the AWS Management Console and AWS Command Line Interface (AWS CLI), [handle this mapping transparently](https://docs.aws.amazon.com/AmazonS3/latest/dev/IndexDocumentSupport.html) for you. For consistency, we recommend that you use lowercase characters for file and folder names.

![Code for a hierarchical file system.](http://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/images/heirarchical-system.jpeg)

## Uploading content
<a name="uploading-content"></a>

 On AWS, you can design your static website using your website authoring tool of choice. Most web design and authoring tools can save the static content on your local hard drive. Then, upload the HTML, images, JavaScript files, CSS files, and other static assets into your Amazon S3 bucket. To deploy, copy any new or modified files to the Amazon S3 bucket. You can use the AWS API, SDKs, or CLI to script this step for a fully automated deployment.

 You can upload files using the AWS Management Console. You can also use AWS partner offerings such as CloudBerry, S3 Bucket Explorer, S3 Fox, and other visual management tools. The easiest way, however, is to use the [AWS CLI](https://aws.amazon.com/cli/)*.* The S3 sync command recursively uploads files and [synchronizes your Amazon S3 bucket](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html) with your local folder. (For moving very large quantities of data into S3, see [https://aws.amazon.com/s3/transfer-acceleration](https://aws.amazon.com/s3/transfer-acceleration/).)

## Making your content publicly accessible
<a name="making-your-content-publicly-accessible"></a>

 For your visitors to access content at the Amazon S3 website endpoint, the Amazon S3 objects must have the appropriate permissions. Amazon S3 enforces a security-by- default policy. New objects in a new bucket are private by default. For example, an Access Denied error appears when trying to view a newly uploaded file using your web browser. To fix this, configure the content as publicly accessible. It’s possible to set object-level permissions for every individual object, but that quickly becomes tedious.

 Instead, define an Amazon S3 bucket-wide policy.

 The following sample Amazon S3 bucket policy enables everyone to view all objects in a bucket:

```
{
       Version":"2012-10-17",

       Statement":[{
       Sid":"PublicReadGetObject",
       Effect":"Allow",

           "Principal": "*",
           "Action":["s3:GetObject"],

           "Resource":["arn:aws:s3:::S3_BUCKET_NAME_GOES_HERE/*"]
        }

    ]

}
```

 This policy defines who can view the contents of your S3 bucket. Refer to the [Securing administration access to your website resources](securing-administration-access-to-your-website-resources.md) section of this document for the AWS Identity and Access Management (IAM) policies to manage permissions for your team members.

 Together, S3 bucket policies and IAM policies give you fine-grained control over who can manage and view your website.

## Requesting a certificate through ACM
<a name="requesting-a-certificate-through-acm"></a>

 You can create and manage [public, private, and imported certificates](https://aws.amazon.com/certificate-manager/faqs/) with ACM. This section focuses on creating and using public certificates to be used with services that integrate with ACM, specifically Amazon Route 53 and Amazon CloudFront.

 **To request a certificate:**

1.  Add in the qualified domain names (such as `example.com`) you want to secure with a certificate.

1.  Select a validation method. ACM can validate ownership by using DNS or by sending email to the contact addresses of the domain owner.

1.  Review the domain names and validation method.

1.  Validate. If you used the DNS validation method, you must create a `CNAME` record in the DNS configuration for each of the domains. If the domain is not currently managed by Amazon Route 53, you can choose to export the DNS configuration file and input that information in your DNS web service. If the domain is managed by Amazon Route 53, you can click “Create record in Route 53” and ACM can update your DNS configuration for you.

 After validation is complete, return to the ACM console. Your certificate status changes from Pending Validation to Issued.

## Low costs encourage experimentation
<a name="low-costs-encourage-experimentation"></a>

 Amazon S3 costs are storage plus bandwidth. The actual costs depend upon your asset file sizes, and your site’s popularity (the number of visitors making browser requests).

 There’s no minimum charge and no setup costs.

 When you use Amazon S3, you pay for what you use. You’re only [charged for the actual Amazon S3 storage required to store the site assets](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketBilling.html). These assets include HTML files, images, JavaScript files, CSS files, videos, audio files, and any other downloadable files. Your bandwidth charges depend upon the actual site traffic. More specifically, the number of bytes that are delivered to the website visitor in the HTTP responses. Small websites with few visitors have minimal hosting costs.

 Popular websites that serve up large videos and images incur higher bandwidth charges. The *Estimating and Tracking AWS Spend* section of this document describes how you can estimate and track your costs.

 With Amazon S3, experimenting with new ideas is easy and cheap. If a website idea fails, the costs are minimal. For microsites, publish many independent microsites at once, run A/B tests, and keep only the successes.
