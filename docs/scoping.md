# Semantic HTML for Scientific Research Institution Annual Reports
## Research Findings and Recommendations

**Date:** January 8, 2026  
**Prepared for:** Assessment Project Team  
**Purpose:** Analysis of existing schemas and examples for converting annual reports from National and International scientific research institutions into structured semantic HTML

---

## Executive Summary

This document addresses two key questions:
1. **Q: Are there existing schemas specifically for scientific research institution annual reports in semantic HTML?**
2. **Q: Are there examples of institutions that create reports in semantic HTML?**

**Key Findings:**
- Multiple established schemas exist that can be adapted for scientific annual reports
- Direct examples of institutions publishing annual reports in semantic HTML are limited
- However, several initiatives demonstrate semantic web technologies applied to scientific reporting
- A combination of Schema.org, Dublin Core, and scientific knowledge graph approaches provides a comprehensive foundation

---

## 1. Existing Schemas for Scientific Research Institution Annual Reports

### 1.1 Schema.org

**Overview:** Schema.org is a collaborative vocabulary developed by major search engines (Google, Microsoft, Yahoo, Yandex) for embedding structured data into web pages using microdata, RDFa, or JSON-LD.

**Relevant Schema.org Types for Annual Reports:**

#### Organization-Level Schemas:
- **`Organization`** / **`ResearchOrganization`**: For the institution itself
  - Properties: `name`, `url`, `address`, `contactPoint`, `foundingDate`, `numberOfEmployees`
  - Can include `department` (for research divisions/departments)

#### Research Output Schemas:
- **`ResearchProject`**: For individual research projects
  - Properties: `name`, `description`, `funder`, `startDate`, `endDate`, `member`
  
- **`ScholarlyArticle`**: For publications mentioned in the report
  - Properties: `headline`, `author`, `datePublished`, `publisher`, `about` (subject matter)
  
- **`Dataset`**: For datasets produced or referenced
  - Properties: `name`, `description`, `creator`, `datePublished`, `distribution`, `keywords`
  
- **`CreativeWork`**: General schema for reports, presentations, and other outputs
  - Properties: `name`, `author`, `datePublished`, `about`, `keywords`

#### Scientific Component Schemas:
- **`BioChemEntity`**: For biological and chemical entities
  - Subtypes include: `Gene`, `Protein`, `MolecularEntity`
  - Properties: `name`, `identifier`, `associatedDisease`, `hasBioChemEntityPart`
  
- **`ChemicalSubstance`**: For chemicals and compounds
  - Properties: `name`, `identifier`, `chemicalComposition`, `potentialUse`
  
- **`Thing`** with specialized properties:
  - Can be extended with custom properties for organisms, equipment, etc.
  - Use `identifier` property to link to external databases (NCBI, ChEBI, etc.)

**Implementation Formats:**
- JSON-LD (recommended for HTML)
- Microdata
- RDFa

**Advantages:**
- Widely supported by search engines
- Enhances discoverability
- Standardized vocabulary
- Can be validated using Google's Rich Results Test

**Limitations:**
- May need extension for domain-specific scientific entities
- Less granular than specialized scientific ontologies

---

### 1.2 Dublin Core Metadata Initiative (DCMI)

**Overview:** DCMI provides a set of vocabulary terms for describing resources, widely used for document metadata.

**Relevant Elements:**
- **Core Elements:**
  - `dc:title` - Report title
  - `dc:creator` - Institution/authors
  - `dc:subject` - Keywords/topics
  - `dc:description` - Abstract/summary
  - `dc:publisher` - Publishing institution
  - `dc:date` - Publication date
  - `dc:type` - Resource type (e.g., "Annual Report")
  - `dc:format` - File format
  - `dc:identifier` - DOI, URL, or other identifier
  - `dc:language` - Language of the report
  - `dc:relation` - Related resources
  - `dc:coverage` - Temporal/spatial coverage
  - `dc:rights` - Copyright/licensing information

**Implementation:**
- Can be embedded in HTML using RDFa or microdata
- Often used alongside Schema.org

**Advantages:**
- Well-established standard
- Simple and widely understood
- Good for basic metadata

**Limitations:**
- Less specific for scientific entities
- Primarily designed for document-level metadata, not fine-grained components

---

### 1.3 Open Research Knowledge Graph (ORKG)

**Overview:** ORKG is an infrastructure project developed by TIB - Leibniz Information Centre for Science and Technology, aimed at improving scholarly communication through structured, semantically rich representations of research contributions.

**Key Features:**
- Decomposes research outputs into fine-grained semantic entities
- Templates for different research contribution types
- Supports comparison and intelligent search
- Machine-readable format

**Relevant Concepts:**
- Research problems
- Methods
- Results
- Materials (can include chemicals, organisms, equipment)
- Software/tools

**Implementation:**
- Uses RDF/OWL ontologies
- Can be exported as JSON-LD
- Provides API for integration

**Advantages:**
- Specifically designed for scientific research
- Fine-grained semantic decomposition
- Supports advanced services (comparison, search)

**Limitations:**
- Primarily focused on research papers, not annual reports
- Requires adaptation for report structure
- Less directly applicable to HTML embedding

---

### 1.4 Micropublications

**Overview:** A semantic model designed for scientific claims, evidence, arguments, and annotations, particularly in biomedical communications.

**Key Features:**
- Formalizes argument structure of scientific publications
- Makes internal structure semantically clear and computable
- Supports claims, evidence, arguments, and annotations

**Relevant Concepts:**
- Scientific claims
- Supporting evidence
- Arguments
- Annotations

**Advantages:**
- Excellent for representing scientific reasoning
- Useful for detailed scientific content

**Limitations:**
- More complex than needed for annual reports
- Primarily designed for publications, not reports
- May be overkill for summary-level reporting

---

### 1.5 Data Catalog Vocabulary (DCAT)

**Overview:** DCAT is designed to facilitate interoperability between data catalogs published on the web.

**Relevant Concepts:**
- `dcat:Dataset` - For datasets mentioned in reports
- `dcat:Catalog` - For collections of datasets
- `dcat:Distribution` - For how datasets are accessed

**Use Case:**
- Particularly useful if annual reports reference or describe datasets
- Can complement Schema.org Dataset markup

---

### 1.6 Scientific Domain-Specific Ontologies

While not directly for HTML markup, these ontologies can inform the structure:

#### Chemical Entities:
- **ChEBI** (Chemical Entities of Biological Interest): Ontology for chemical entities
- **PubChem**: Database with semantic identifiers for chemicals
- Can be referenced via `identifier` properties in Schema.org

#### Biological Entities:
- **NCBI Taxonomy**: For organisms and species
- **Gene Ontology**: For gene and protein functions
- **UniProt**: For protein information
- Can be linked via identifiers in semantic HTML

#### Equipment/Instruments:
- Less standardized ontologies exist
- May require custom Schema.org extensions or use of `Thing` with `identifier` properties

---

## 2. Examples of Institutions Using Semantic HTML in Reports

### 2.1 Direct Examples (Limited)

**Finding:** Specific examples of institutions publishing annual reports in semantic HTML are **limited**. Most institutions still publish annual reports as PDFs or basic HTML without semantic markup.

**Possible Reasons:**
- Annual reports are often produced as PDFs for print compatibility
- Semantic HTML requires additional effort and expertise
- Benefits may not be immediately obvious to institutions
- Focus has been on publications rather than reports

### 2.2 Related Initiatives Demonstrating Semantic Technologies

While direct examples are limited, several initiatives demonstrate the application of semantic web technologies to scientific information:

#### 2.2.1 Open Research Knowledge Graph (ORKG)
- **Institution:** TIB - Leibniz Information Centre for Science and Technology (Germany)
- **What they do:** Create structured, semantically rich representations of research contributions
- **Relevance:** Shows how scientific outputs can be decomposed into semantic entities
- **URL:** https://www.orkg.org/
- **Takeaway:** Demonstrates fine-grained semantic decomposition of research outputs

#### 2.2.2 SemOpenAlex
- **What it is:** Extensive RDF knowledge graph containing over 26 billion triples about scientific publications and associated entities
- **Entities included:** Authors, institutions, journals, concepts, publications
- **Relevance:** Shows scalability of semantic representations for scientific information
- **Takeaway:** Demonstrates how large-scale scientific data can be structured semantically

#### 2.2.3 SciKGTeX
- **What it is:** LaTeX package that enables authors to semantically annotate contributions in scientific publications
- **How it works:** Embeds marked contributions as metadata into generated PDF documents
- **Relevance:** Shows practical workflow for semantic annotation
- **Takeaway:** Demonstrates that semantic annotation can be integrated into document creation workflows

#### 2.2.4 OntoMetric Framework
- **What it is:** Ontology-guided framework that transforms ESG (Environmental, Social, and Governance) regulatory documents into validated, AI- and web-ready knowledge graphs
- **Relevance:** Shows conversion of unstructured documents into structured, semantically rich formats
- **Takeaway:** Demonstrates that complex reports can be transformed into semantic formats

#### 2.2.5 CrossRef's Reports and Working Papers Markup Guide
- **What it is:** Guidelines for marking up reports and working papers using XML
- **Relevance:** Provides structured approach to representing report metadata
- **Takeaway:** Shows that structured markup for reports is recognized as valuable

### 2.3 W3C Semantic Web for Life Sciences Workshop

- **What it is:** Workshop organized by W3C focused on application of Semantic Web technologies in life sciences
- **Relevance:** Indicates trend towards semantic representation in scientific communications
- **Takeaway:** Scientific community recognizes value of semantic technologies

---

## 3. Recommendations for Implementation

### 3.1 Recommended Schema Combination

**Primary Schema:** Schema.org
- Use for main structure and common entities
- Provides good search engine support
- Widely recognized

**Complementary Schemas:**
- **Dublin Core:** For basic metadata (title, creator, date, etc.)
- **DCAT:** If datasets are a major component
- **Custom extensions:** For domain-specific scientific entities not covered by Schema.org

### 3.2 Implementation Approach

#### 3.2.1 Document Structure
```html
<!-- Document-level metadata -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Report",
  "name": "Annual Report 2025",
  "publisher": {
    "@type": "ResearchOrganization",
    "name": "Institution Name"
  },
  "datePublished": "2025-01-08",
  "about": [...]
}
</script>
```

#### 3.2.2 Research Projects
```html
<div itemscope itemtype="https://schema.org/ResearchProject">
  <h2 itemprop="name">Project Title</h2>
  <p itemprop="description">Project description...</p>
  <meta itemprop="startDate" content="2024-01-01">
  <meta itemprop="endDate" content="2024-12-31">
</div>
```

#### 3.2.3 Scientific Components

**Chemicals:**
```html
<span itemscope itemtype="https://schema.org/ChemicalSubstance">
  <span itemprop="name">Aspirin</span>
  <meta itemprop="identifier" content="https://pubchem.ncbi.nlm.nih.gov/compound/2244">
</span>
```

**Organisms:**
```html
<span itemscope itemtype="https://schema.org/Thing">
  <span itemprop="name">Escherichia coli</span>
  <meta itemprop="identifier" content="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=562">
</span>
```

**Genes:**
```html
<span itemscope itemtype="https://schema.org/BioChemEntity">
  <span itemprop="name">BRCA1</span>
  <meta itemprop="identifier" content="https://www.ncbi.nlm.nih.gov/gene/672">
</span>
```

**Equipment:**
```html
<span itemscope itemtype="https://schema.org/Thing">
  <span itemprop="name">Mass Spectrometer</span>
  <meta itemprop="description" content="Model XYZ-123">
</span>
```

### 3.3 Fine-Grained Indexing Strategy

1. **Identify all scientific components** in the text:
   - Chemicals (using PubChem/ChEBI identifiers)
   - Organisms (using NCBI Taxonomy identifiers)
   - Genes/Proteins (using NCBI Gene/UniProt identifiers)
   - Equipment (may require custom approach)

2. **Mark up each component** with appropriate Schema.org types

3. **Create an index section** that aggregates all marked-up components:
   - Group by type (Chemicals, Organisms, Genes, Equipment)
   - Link to sections where they appear
   - Include identifiers for external databases

4. **Use consistent identifiers** linking to authoritative sources:
   - PubChem for chemicals
   - NCBI Taxonomy for organisms
   - NCBI Gene for genes
   - UniProt for proteins

### 3.4 Key Outputs Section

Structure key outputs using:
- `ResearchProject` for projects
- `ScholarlyArticle` for publications
- `Dataset` for datasets
- `CreativeWork` for other outputs (presentations, software, etc.)

Each output should include:
- Title/name
- Description
- Authors/contributors
- Date
- Related scientific components (linked via `about` or custom properties)

---

## 4. Challenges and Considerations

### 4.1 Technical Challenges

1. **Volume of markup:** Annual reports can be lengthy; manual markup is time-consuming
2. **Entity recognition:** Automatically identifying scientific components requires NLP/NER tools
3. **Identifier resolution:** Linking to correct external database identifiers
4. **Validation:** Ensuring markup is correct and complete

### 4.2 Content Challenges

1. **Granularity:** Deciding how fine-grained to make the markup
2. **Consistency:** Ensuring consistent markup across sections
3. **Completeness:** Ensuring all relevant components are marked up

### 4.3 Maintenance Challenges

1. **Updates:** Keeping markup current as reports are updated
2. **Standards evolution:** Schema.org and other standards evolve
3. **Tooling:** Need for tools to generate and validate markup

---

## 5. Tools and Resources

### 5.1 Validation Tools

- **Google Rich Results Test:** https://search.google.com/test/rich-results
- **Schema.org Validator:** Various online validators available
- **W3C Markup Validator:** For HTML validation

### 5.2 Entity Recognition Tools

- **spaCy:** NLP library with biomedical models
- **scispacy:** Specialized spaCy models for scientific text
- **PubTator:** For biomedical entity recognition
- **ChemDataExtractor:** For chemical entity extraction

### 5.3 Identifier Resolution

- **PubChem:** https://pubchem.ncbi.nlm.nih.gov/
- **NCBI Taxonomy:** https://www.ncbi.nlm.nih.gov/taxonomy
- **NCBI Gene:** https://www.ncbi.nlm.nih.gov/gene
- **UniProt:** https://www.uniprot.org/
- **ChEBI:** https://www.ebi.ac.uk/chebi/

---

## 6. Next Steps

### 6.1 Immediate Actions

1. **Review existing annual reports** to understand structure and content
2. **Identify key scientific components** that need indexing
3. **Choose primary schema** (recommendation: Schema.org with Dublin Core)
4. **Create markup template** based on report structure

### 6.2 Short-Term Development

1. **Develop entity recognition pipeline** for scientific components
2. **Create identifier resolution service** for linking to external databases
3. **Build markup generation tool** to automate semantic HTML creation
4. **Develop validation tools** to ensure markup quality

### 6.3 Long-Term Goals

1. **Establish markup standards** for the institution
2. **Create reusable templates** for annual reports
3. **Develop search/indexing capabilities** over semantic markup
4. **Integrate with knowledge graphs** (e.g., ORKG) if appropriate

---

## 7. References and Further Reading

### 7.1 Schema Documentation

- Schema.org: https://schema.org/
- Schema.org Organization: https://schema.org/Organization
- Schema.org ResearchProject: https://schema.org/ResearchProject
- Schema.org Dataset: https://schema.org/Dataset
- Schema.org ScholarlyArticle: https://schema.org/ScholarlyArticle
- Schema.org BioChemEntity: https://schema.org/BioChemEntity

### 7.2 Standards and Initiatives

- Dublin Core Metadata Initiative: https://www.dublincore.org/
- Data Catalog Vocabulary (DCAT): https://www.w3.org/TR/vocab-dcat-2/
- Open Research Knowledge Graph: https://www.orkg.org/
- W3C Semantic Web: https://www.w3.org/standards/semanticweb/

### 7.3 Research Papers

- Micropublications: https://arxiv.org/abs/1305.3506
- SciKGTeX: https://arxiv.org/abs/2304.05327
- SemOpenAlex: https://arxiv.org/abs/2308.03671
- OntoMetric Framework: https://arxiv.org/abs/2512.01289

### 7.4 Tools and Resources

- Google Rich Results Test: https://search.google.com/test/rich-results
- PubChem: https://pubchem.ncbi.nlm.nih.gov/
- NCBI Taxonomy: https://www.ncbi.nlm.nih.gov/taxonomy
- NCBI Gene: https://www.ncbi.nlm.nih.gov/gene
- UniProt: https://www.uniprot.org/
- ChEBI: https://www.ebi.ac.uk/chebi/

---

## 8. Conclusion

### 8.1 Summary of Findings

**Question 1: Are there existing schemas specifically for scientific research institution annual reports?**

**Answer:** While there are no schemas *specifically* designed for annual reports, multiple established schemas can be effectively combined:
- **Schema.org** provides the best foundation with types for Organization, ResearchProject, Dataset, ScholarlyArticle, and scientific entities
- **Dublin Core** complements for basic metadata
- **DCAT** useful if datasets are prominent
- **Scientific knowledge graphs** (ORKG) provide inspiration for fine-grained decomposition

**Question 2: Are there examples of institutions that create reports in semantic HTML?**

**Answer:** Direct examples are **limited**, but several related initiatives demonstrate the value and feasibility:
- ORKG shows semantic decomposition of research outputs
- SemOpenAlex demonstrates scalability
- SciKGTeX shows practical annotation workflows
- OntoMetric demonstrates document transformation to semantic formats

### 8.2 Recommendations

1. **Adopt Schema.org as primary schema** with Dublin Core for metadata
2. **Use JSON-LD format** for embedding structured data in HTML
3. **Link scientific components to authoritative databases** (PubChem, NCBI, etc.)
4. **Develop automated tools** for entity recognition and markup generation
5. **Create templates** based on report structure
6. **Validate markup** using available tools

### 8.3 Expected Benefits

- **Enhanced discoverability:** Search engines can better understand content
- **Improved indexing:** Fine-grained index of scientific components
- **Interoperability:** Standard formats enable integration with other systems
- **Machine readability:** Enables automated processing and analysis
- **Future-proofing:** Semantic markup supports emerging AI/ML applications

---

**Document prepared:** January 8, 2026  
**Status:** Research complete, ready for implementation planning

