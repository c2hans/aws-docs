---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/aws-products-in-gxp-systems.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Products in GxP Systems
<a name="aws-products-in-gxp-systems"></a>

 With limited technical guidance from regulatory and industry bodies, this section aims to describe some of the best practices we’ve seen customers adopting when using cloud services to meet their regulatory compliance needs.

 The Final FDA Guidance Document, “[Data Integrity and Compliance With Drug CGMP](https://www.fda.gov/media/119267/download)” explicitly brings cloud infrastructure into scope through the revised definition of “computer or related systems”:

 “The American National Standards Institute (ANSI) defines systems as people, machines, and methods organized to accomplish a set of specific functions. Computer or related systems can refer to computer hardware, software, peripheral devices, networks, **cloud infrastructure**, personnel and associated documents (e.g., user manuals and standard operating procedures).“

 Further, industry organizations like ISPE are increasingly dedicating publications on cloud usage in the life sciences.

 As described throughout this whitepaper, there is no unique certification for GxP regulations so each customer defines their own risk profile. Therefore, it is important to note that although this whitepaper is based on AWS experience with life science customers, you must take final accountability and determine your own regulatory obligations.

 To begin with, even when deployed in the cloud, GxP applications still need to be validated and their underlying infrastructure still needs qualifying. The basic principles governing on-premise infrastructure qualification still apply to virtualized cloud infrastructure. Therefore, the current industry guidance should still be leveraged.

 Traditionally, a regulated company was accountable and responsible for all aspects of their infrastructure qualification and application validation. With the introduction of public cloud providers, part of that responsibility has been shifted to a cloud supplier. The regulated company is still accountable, but the cloud supplier is now responsible for the qualification of the physical infrastructure, virtualization and service layers and to completely manage the services they provide, i.e. the big difference now is that there is a shared compliance responsibility model which is similar to the shared security responsibility model described earlier in this whitepaper.

 Previous sections of this whitepaper described how AWS takes care of their part of the shared responsibility model. This section provides recommended strategies on how to cover your part of the shared responsibility model for GxP environments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
