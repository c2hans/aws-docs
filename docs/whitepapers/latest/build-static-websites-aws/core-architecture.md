---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/core-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Core architecture
<a name="core-architecture"></a>

 In a traditional (non-AWS) architecture, web servers serve up static content. Typically, content is managed using a content management system (CMS), and multiple static sites are hosted on the same infrastructure. The content is stored on local disks, or on a file share on network-accessible storage. The following example shows a sample file system structure.

```
    ├─ css/
    │ ├─ main.css
    │ └─ navigation.css
    ├─ images/
    │ ├─ banner.jpg
    │ └─ logo.jpg
    ├─ index.html
    ├─ scripts/
    │ ├─ script1.js
    │ └─ script2.js
    ├─ section1.html
    └─ section2.html
```

A network firewall protects against unauthorized access. It’s common to deploy multiple web servers behind a load balancer for high availability (HA) and scalability. Since pages are static, the web servers don’t need to maintain any state or session information and the load balancer doesn’t need to implement session affinity (“sticky sessions”). The following diagram shows a traditional (non-AWS) hosting environment:

![A diagram depciting the basic architecture of a traditional hosting environment .](http://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/images/traditional-hosting.jpeg)
