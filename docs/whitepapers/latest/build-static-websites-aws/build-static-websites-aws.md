---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/build-static-websites-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Hosting Static Websites on AWS
<a name="build-static-websites-aws"></a>

Publication date: **May 21, 2021** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 This whitepaper covers comprehensive architectural guidance for developing, deploying, and managing static websites on Amazon Web Services (AWS) while keeping operational simplicity and business requirements in mind. We also recommend an approach that provides insignificant cost of operation, little or no management required, and a highly scalable, resilient, and reliable website.

 This whitepaper first reviews how static websites are hosted in traditional hosting environments. Then, we explore a simpler and more cost-efficient approach using [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3). Finally, we show you how you can enhance the AWS architecture by encrypting data in transit and to layer on functionality and improve quality of service by using Amazon CloudFront.

### Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

### Introduction
<a name="introduction"></a>

 As enterprises become more digital operations, their websites span a wide spectrum, from mission-critical e-commerce sites to departmental apps, and from business-to-business (B2B) portals to marketing sites. Factors such as business value, mission criticality, service level agreements (SLAs), quality of service, and information security drive the choice of architecture and technology stack.

 The simplest form of website architecture is the *static website*, where users are served static content (HTML, images, video, JavaScript, style sheets, and so on). Some examples include brand microsites, marketing websites, and intranet information pages. Static websites are straightforward in one sense, but they can still have demanding requirements in terms of scalability, availability, and service-level guarantees. For example, a marketing site for a consumer brand may need to be prepared for an unpredictable onslaught of visitors when a new product is launched.

#### Static website
<a name="static-website"></a>

 A static website delivers content in the same format in which it is stored. No server-side code execution is required. For example, if a static website consists of HTML documents displaying images, it delivers the HTML and images as-is to the browser, without altering the contents of the files.

 Static websites can be delivered to web browsers on desktops, tablets, or mobile devices. They usually consist of a mix of HTML documents, images, videos, CSS stylesheets, and JavaScript files. Static doesn’t have to mean boring—static sites can provide client-side interactivity as well. Using HTML5 and client-side JavaScript technologies such as jQuery, AngularJS, React, and Backbone, you can deliver rich user experiences that are engaging and interactive.

 Some examples of static sites include:
+  Marketing websites
+  Product landing pages
+  Microsites that display the same content to all users
+  Team homepages
+  A website that lists available assets (for example., image files, video files, and press releases) allows the user to download the files as-is
+  Proofs-of-concept used in the early stages of web development to test user experience flows and gather feedback

 Static websites load quickly since content is delivered as-is and can be cached by a content delivery network (CDN). The web server doesn’t need to perform any application logic or database queries. They’re also relatively inexpensive to develop and host.

 However, maintaining large static websites can be cumbersome without the aid of automated tools, and static websites can’t deliver personalized information.

 Static websites are most suitable when the content is infrequently updated. After the content evolves in complexity or needs to be frequently updated, personalized, or dynamically generated, it's best to consider a dynamic website architecture.

#### Dynamic website
<a name="dynamic-website"></a>

 Dynamic websites can display dynamic or personalized content. They usually interact with data sources and web services, and require code development expertise to create and maintain. For example, a sports news site can display information based on the visitor's preferences, and use server-side code to display updated sport scores. Other examples of dynamic sites are e-commerce shopping sites, news portals, social networking sites, finance sites, and most other websites that display ever-changing information.
