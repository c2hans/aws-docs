---
source_url: https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-cards-intro.html
---

# Infrastructure Composer cards
<a name="using-composer-cards-intro"></a>

Infrastructure Composer simplifies the process of writing infrastructure as code (IaC) for CloudFormation resources. To effectively use Infrastructure Composer, there are two basic concepts you should first understand: Infrastructure Composer [cards](#using-composer-cards-intro) and [card connections](using-composer-connecting.md).

In Infrastructure Composer, cards represent CloudFormation resources. there are two general categories of cards:
+ [Enhanced component card](using-composer-cards-component-intro-enhanced.md) – A collection of CloudFormation resources that have been combined into a single curated card that enhances ease of use, functionality, and are designed for a wide variety of use cases. Enhanced component cards are the first cards listed in the **Resources** palette in Infrastructure Composer.
+ [Standard IaC resource card](using-composer-cards-resource-intro.md) – A single AWS CloudFormation resource. Each standard IaC resource card, once dragged onto the canvas, is labeled **Standard component** and may be combined into multiple resources.

**Note**
Depending on the card, a *Standard IaC resource* card may be labeled a **Standard component** card after it has been dragged onto the visual canvas. This simply means the card is a collection of one or more standard IaC resource cards.

While some types of cards are available from the **Resources** palette, cards can also appear on the canvas when you import an existing CloudFormation or AWS Serverless Application Model (AWS SAM) template into Infrastructure Composer. The following image is an example of an imported application that contains various card types:

![An imported application template displayed on the Infrastructure Composer canvas, showing various card types.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_cards_11.png)

**Topics**
+ [Enhanced component cards in Infrastructure Composer](using-composer-cards-component-intro-enhanced.md)
+ [Standard component cards in Infrastructure Composer](using-composer-cards-resource-intro.md)
+ [Card connections in Infrastructure Composer](using-composer-connecting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Infrastructure Composer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query infrastructure-composer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
