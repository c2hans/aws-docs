---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/instance-choice.html
---

# Choosing the instance type
<a name="instance-choice"></a>

F5 supports multiple instance types and choosing which one to use can be a complex decision. For most migrations, `c5n.2xl` and `c5n.4xl` will be the most common instance choices because they offer a mix of network performance, CPU density, interface density, and the number of IPs that can be supported on the instance. The following diagram provides examples of which instances to choose, based on the F5 products you are using.

![Process flow for choosing which instance type to use.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/images/guide-img/migration-f5-big-ip/images/F5-instance-choice.png)
