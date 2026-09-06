---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/accelerating-content-delivery.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Accelerating content delivery
<a name="accelerating-content-delivery"></a>

 Any WordPress website needs to deliver a mix of static and dynamic content. Static content includes images, JavaScript files, or style sheets. Dynamic content includes anything generated on the server side using the WordPress PHP code, for example, elements of your site that are generated from the database or personalized to each viewer.

An important aspect of the end-user experience is the network latency involved when delivering the previous content to users around the world. Accelerating the delivery of the previous content improves the end-user experience, especially users geographically spread across the globe. This can be achieved with a Content Delivery Network (CDN) such as Amazon CloudFront.

 [Amazon CloudFront](https://aws.amazon.com/cloudfront/) is a web service that provides an easy and cost-effective way to distribute content with low latency and high data transfer speeds through multiple edge locations across the globe. Viewer requests are automatically routed to a suitable CloudFront [edge location](https://aws.amazon.com/cloudfront/details/#edge-locations) to lower the latency. If the content can be cached (for a few seconds, minutes, or even days) and is already stored in a particular edge location, CloudFront delivers it immediately. If the content should not be cached, has expired, or isn’t currently in that edge location, CloudFront retrieves content from one or more sources of truth, referred to as the origin(s) (in this case, the Lightsail instance) in the CloudFront configuration. This retrieval takes place over optimized network connections, which work to speed up the delivery of content on your website. Apart from improving the end-user experience, the model discussed also reduces the load on your origin servers and has the potential to create significant cost savings.
