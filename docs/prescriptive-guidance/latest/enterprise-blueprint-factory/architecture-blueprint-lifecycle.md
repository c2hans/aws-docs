---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/enterprise-blueprint-factory/architecture-blueprint-lifecycle.html
---

# Blueprint life cycle in the Enterprise Blueprint Factory
<a name="architecture-blueprint-lifecycle"></a>

The life cycle of an Enterprise Blueprint Factory blueprint consists of three typical stages: creation, update, and deletion. The life cycle stage affects which actions that the config pipeline and release pipeline perform.

## Blueprint creation
<a name="architecture-blueprint-lifecycle-create"></a>

To release a new blueprint as a product in AWS Service Catalog, a developer merges the blueprint into the product repository, updates the portfolios in the config file, and adds the new product to the config file. This invokes the configuration pipeline. The config pipeline creates a release pipeline** **for the product. In the release pipeline, the blueprint undergoes multiple security checks. The release pipeline then deploys the blueprint as a Service Catalog product.

![Config and release pipeline actions when you create a blueprint.](http://docs.aws.amazon.com/prescriptive-guidance/latest/enterprise-blueprint-factory/images/guide-img/fbe4d444-882e-464d-9768-c5b4c6cfd79b/images/e76467ab-6d6c-4efa-a282-d5e20ce35c64.png)

## Blueprint update
<a name="architecture-blueprint-lifecycle-update"></a>

A developer can update the product in Service Catalog by merging an updated version of the blueprint into the product repository. This update invokes the release pipeline for the product. The updated template undergoes the security checks in the release pipeline. The release pipeline deploys a new version of the Service Catalog product. For more information about how Service Catalog updates the product version, see [Managing versions](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/managing-versions.html) in the Service Catalog documentation.

![Release pipeline actions when you update a blueprint.](http://docs.aws.amazon.com/prescriptive-guidance/latest/enterprise-blueprint-factory/images/guide-img/fbe4d444-882e-464d-9768-c5b4c6cfd79b/images/4381c048-f34c-4466-8fbf-80a13f577fac.png)

Alternatively, you can update which Service Catalog portfolio the blueprint is associated with or you can change the sharing configurations for those portfolios. In this case, the developer updates the config file in the configuration repo. The configuration pipeline updates the portfolios or portfolio shares. In this case, the product in Service Catalog is unchanged, although it may now be included in different portfolios.

![Config pipeline actions when you update a portfolio or portfolio share.](http://docs.aws.amazon.com/prescriptive-guidance/latest/enterprise-blueprint-factory/images/guide-img/fbe4d444-882e-464d-9768-c5b4c6cfd79b/images/94256e0a-14c9-4e40-beb1-0093d7b62783.png)

## Blueprint deletion
<a name="architecture-blueprint-lifecycle-delete"></a>

**Important**
You cannot recover a Service Catalog product after it is deleted. However, you can redeploy the blueprint as a new product.

When you delete a product, Service Catalog removes all of product versions from every portfolio that contains the product. For more information, see [Deleting products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/productmgmt-delete.html) in the Service Catalog documentation.

To delete a blueprint after it has been deployed in Service Catalog, a developer deletes the blueprint in the product repo. Then they remove the product from the config file. The config pipeline disassociates the product from the portfolios that contain it and deletes all product associates. The release pipeline terminates the Service Catalog product and the [provisioned products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is_concepts.html#what-is_concepts-provprod). Then, the config pipeline deletes the product's release pipeline.

If the config pipeline is unable to disassociate all of the product's resources, then the product is not deleted and the pipeline fails. You must resolve the failed resource disassociation and then restart the pipeline. For more information, see [Resolving failed resource disassociations when deleting a product](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/product-delete-exception.html).

![Config and release pipeline actions when you delete a blueprint.](http://docs.aws.amazon.com/prescriptive-guidance/latest/enterprise-blueprint-factory/images/guide-img/fbe4d444-882e-464d-9768-c5b4c6cfd79b/images/063713f0-5768-47e2-b875-228f643a219b.png)
