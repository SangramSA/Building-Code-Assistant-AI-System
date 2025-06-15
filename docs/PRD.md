# Product Requirements Document: Building Code Assistant AI System - Personal Project MVP (Updated)

**Version:** 1.1 Personal Project - Hybrid Approach  
**Date:** May 30, 2025  
**Team:** 2-Person Personal Project  
**Timeline:** 3-4 Months (Flexible)  

---

## 1. Project Overview

### 1.1 Project Vision

Build a personal learning project that demonstrates AI/ML skills while creating a useful tool for building code queries. This serves as both a technical portfolio piece and a proof-of-concept for Graph RAG implementation in a real-world domain, with emphasis on understanding both custom implementation and framework evaluation.

### 1.2 Personal Learning Objectives

- **Primary:** Master Graph RAG architecture through custom implementation AND framework comparison
- **Secondary:** Build production-ready AI application demonstrating technical decision-making
- **Tertiary:** Create impressive portfolio piece showcasing both foundational knowledge and practical engineering judgment
- **Bonus:** Validate business concept while demonstrating ability to evaluate and adopt appropriate tools

### 1.3 Project Success Criteria

- **Technical:** Successfully implement working Graph RAG system with hybrid custom/framework approach
- **Learning:** Gain deep understanding of vector databases, knowledge graphs, LLM integration, AND framework trade-offs
- **Portfolio:** Create demonstrable project showing both foundational skills and engineering judgment
- **Validation:** Confirm concept utility while documenting technical decision-making process

---

## 2. Project Scope

### 2.1 MVP Goals

- Build working AI assistant for Philadelphia building codes using phased implementation approach
- Demonstrate Graph RAG capabilities with both custom and framework components
- Create well-documented comparison of custom vs. framework approaches
- Document technical decision-making process for portfolio value

### 2.2 What We're Building

- Web-based AI assistant for building code questions
- Graph database + vector search + LLM integration (hybrid implementation)
- Comparative analysis of custom vs. framework approaches
- Clean, well-documented codebase showing engineering judgment
- Technical documentation explaining architecture decisions

### 2.3 What We're NOT Building (For Now)

- Commercial product with user accounts
- Multi-jurisdiction support
- Mobile apps
- Enterprise features
- Monetization mechanisms
- Large-scale infrastructure

---

## 3. Technical Learning Goals

### 3.1 Skills to Develop/Demonstrate

#### Person 1 Focus Areas:
- **Graph Databases:** Neo4j implementation and Cypher queries
- **Vector Databases:** Embedding generation and similarity search
- **LLM Integration:** Prompt engineering and context management
- **Framework Evaluation:** Custom implementation vs. LangChain/LangGraph
- **Technical Decision Making:** When to build vs. buy/use frameworks
- **Data Processing:** PDF extraction and knowledge graph construction
- **API Development:** FastAPI and backend architecture

#### Person 2 Focus Areas:
- **Streamlit Development:** Rapid AI application prototyping
- **Data Visualization:** Streamlit charts and display components
- **AI/ML Integration:** Streamlit integration with ML APIs
- **UX for AI Systems:** Designing interfaces for AI interactions within Streamlit constraints
- **Full-Stack Integration:** Streamlit-backend coordination
- **Advanced Frontend Planning:** Research React/Next.js for Phase 2
- **Deployment:** Getting Streamlit applications live and accessible

### 3.2 Shared Learning Goals

- End-to-end AI application development with hybrid architecture
- Working with unstructured data (PDFs, legal documents)
- System architecture decision-making for AI applications
- Performance optimization comparison (custom vs. framework)
- Technical documentation and comparative analysis
- Engineering judgment demonstration through tool selection

---

## 4. Functional Requirements - Personal Project

### 4.1 Core Features (Portfolio Demonstrators)

#### F-001: Intelligent Query Processing
**Learning Focus:** Natural language processing and query understanding  
**Implementation Approach:** 
- **Phase 1:** Custom query classification and routing
- **Phase 2:** Evaluate LangChain query processing utilities
- **Phase 3:** Hybrid approach with documented trade-offs
- Include 20-30 test cases comparing both approaches

#### F-002: Graph RAG Implementation  
**Learning Focus:** Knowledge graph construction and traversal  
**Implementation Approach:**
- **Phase 1:** Build knowledge graph from Philadelphia building codes using custom logic
- **Phase 2:** Evaluate LangGraph for workflow orchestration
- **Phase 3:** Document performance and maintainability comparison
- Demonstrate relationship traversal and context expansion with both approaches

#### F-003: Streamlit Web Interface
**Learning Focus:** Rapid prototyping of AI applications  
**Implementation:**
- Simple, functional interface using Streamlit components
- Support for real-time query processing
- Built-in charts and visualizations for performance metrics
- Easy deployment and sharing capabilities
- Foundation for understanding AI interface requirements before building advanced frontend

#### F-004: Comparative Documentation
**Learning Focus:** Technical decision-making and engineering judgment  
**Implementation:**
- Well-structured, commented codebase for both approaches
- Comparative analysis documentation
- Decision framework explanation
- Performance metrics comparison
- Architecture diagrams for both implementations

### 4.2 Demo-Ready Features

#### F-005: Technical Showcase Scenarios
**Purpose:** Demonstrate system capabilities and technical judgment effectively  
**Implementation:**
- Side-by-side performance comparisons
- Architecture decision explanations
- Trade-off analysis with specific examples
- Cost/benefit analysis of framework adoption
- Timeline and development velocity comparisons

---

## 5. Technical Implementation - Personal Project

### 5.1 Technology Choices (Learning-Focused)

#### Backend Stack:
- **Python:** Core language for AI/ML work
- **FastAPI:** Modern, async API framework
- **Neo4j Community:** Graph database (free version)
- **Sentence Transformers:** Local embedding generation
- **OpenAI API:** For LLM capabilities (cost-effective for learning)
- **Chroma or FAISS:** Vector database (local/free options)
- **LangChain:** Selective adoption for document processing and utilities
- **LangGraph:** Evaluation for workflow orchestration (Phase 2)

#### Frontend Stack:
- **Phase 1:** Streamlit for rapid prototyping and MVP
- **Phase 2:** React + TypeScript for production frontend
- **Styling:** Streamlit built-in components, later Tailwind CSS
- **Rationale:** Focus on core Graph RAG implementation first

#### Infrastructure:
- **Railway/Render:** Easy deployment for personal projects
- **GitHub:** Version control and project showcase with comparative branches
- **Local Development:** Docker for consistent development environment

### 5.2 Data Processing Approach

#### Phased, Comparative Process:
1. **Custom Implementation:** Start with manually built processing pipeline
2. **Framework Evaluation:** Replace components selectively with LangChain
3. **Performance Comparison:** Document speed, accuracy, and maintainability differences
4. **Quality Focus:** Ensure both approaches produce high-quality results
5. **Documentation:** Document every decision for portfolio/learning value

#### Data Sources:
- Philadelphia Building Code (official PDF)
- Focus on ~10-20 most commonly referenced sections
- Parallel processing with both custom and LangChain approaches
- Clear documentation of processing quality differences

### 5.3 Phased Implementation Strategy

#### Phase 1: Custom Implementation (Months 1-2)
**Objective:** Deep understanding of Graph RAG fundamentals
- Build vector search from scratch using FAISS/Chroma directly
- Implement custom graph traversal logic in Neo4j
- Direct LLM API integration with custom prompts
- Manual document processing and embedding generation

#### Phase 2: Selective Framework Adoption (Month 3)
**Objective:** Evaluate where frameworks add value
- Replace document processing with LangChain loaders
- Evaluate LangGraph for workflow orchestration
- Compare custom vs. framework performance and maintainability
- Document decision criteria and trade-offs

#### Phase 3: Hybrid Optimization (Month 4)
**Objective:** Optimal blend of custom and framework code
- Finalize architecture decisions
- Optimize performance of hybrid approach
- Create comprehensive documentation of technical choices
- Prepare comparative analysis for portfolio presentation

### 5.5 Phased Frontend Strategy

#### Phase 1: Streamlit MVP (Months 1-3)
**Objective:** Rapid prototyping and core functionality focus
- Use Streamlit for immediate UI without frontend complexity
- Enable quick iteration on Graph RAG features
- Create functional demo for portfolio and testing
- Focus learning on AI/ML components rather than frontend frameworks

#### Phase 2: Advanced Frontend (Month 4+)
**Objective:** Professional, production-ready interface
- Migrate to React + TypeScript for advanced UI
- Implement custom components and interactions
- Add advanced features like real-time updates, complex visualizations
- Demonstrate full-stack development capabilities

#### Rationale:
- **Learning Focus:** Streamlit allows concentration on Graph RAG implementation
- **Speed:** Faster to demonstrate core value proposition
- **Portfolio Value:** Shows pragmatic technical decision-making
- **Risk Mitigation:** Reduces complexity in initial phases

Criteria for adopting framework components:
- **Time Savings:** Does it significantly reduce development time?
- **Learning Value:** Does using it prevent understanding core concepts?
- **Customization Need:** Can we customize it for building code domain?
- **Maintenance:** Will it be easier to maintain long-term?
- **Portfolio Value:** Does it demonstrate better engineering judgment?

---

## 6. Personal Project Timeline

### 6.1 Updated 3-4 Month Schedule

#### Month 1: Foundation & Custom Implementation
**Week 1-2: Research & Setup**
- Research Graph RAG implementations
- Compare custom implementation vs. LangChain approaches
- Set up development environment
- Document decision-making criteria for framework adoption
- Create project repository with comparative structure

**Week 3-4: Core Custom Components**
- Implement basic graph database with custom logic
- Set up vector search capability using direct FAISS/Chroma integration
- Create initial embeddings with custom processing
- Build basic API structure
- Build custom retrieval logic to understand fundamentals

#### Month 2: Custom Integration & Development
**Week 5-6: Custom Graph RAG Implementation**
- Implement hybrid search with custom logic
- Build custom context assembly logic
- Create direct LLM integration with custom prompts
- Test with sample queries
- Document custom implementation challenges and solutions

**Week 7-8: Streamlit Interface Development + Framework Research**
- Build Streamlit interface for query processing
- Create data visualization components for performance metrics
- Evaluate LangChain document loaders vs. custom implementation
- Research React/Next.js for Phase 2 advanced frontend
- Document trade-offs and initial framework assessment

#### Month 3: Framework Integration & Comparison
**Week 9-10: Selective Framework Adoption**
- Implement LangChain document processing
- Evaluate LangGraph for workflow orchestration
- Create parallel implementations for comparison
- Performance testing and benchmarking

**Week 11-12: Comparative Analysis**
- Side-by-side testing of both approaches
- Document performance, maintainability, and development velocity differences
- Create hybrid approach using best of both
- Update frontend to showcase comparisons

#### Month 4: Optimization & Portfolio Preparation
**Week 13-14: Hybrid System Optimization**
- Finalize optimal architecture combining custom and framework components
- Performance optimization
- Bug fixes and refinements
- Create comprehensive technical documentation

**Week 15-16: Portfolio Preparation & Deployment**
- Deploy live demo with comparative features
- Create technical blog post explaining decisions
- Prepare presentation materials
- Document lessons learned and recommendations

### 6.2 Milestone Flexibility
- **Personal schedules:** Accommodate work/life balance
- **Learning pace:** Spend additional time on interesting comparative analysis
- **Scope adjustment:** Focus more on successful comparisons than feature breadth
- **Documentation focus:** Emphasis on decision-making documentation throughout

---

## 7. Personal Project Resources

### 7.1 Cost Structure (Minimal Budget)

| Item | Monthly Cost | 4-Month Total |
|------|--------------|---------------|
| Streamlit Cloud Hosting | $0-20 | $0-80 |
| OpenAI API Credits | $30-60* | $120-240 |
| Domain Name (optional) | $12/year | $12 |
| **Total Project Cost** | **~$42-92** | **~$132-332** |

*Slightly higher due to comparative testing

### 7.2 Time Investment (Flexible)

| Person | Flexible Hours/Week | Total Commitment |
|--------|-------------------|------------------|
| Person 1 | 12-25 hours | 192-400 hours |
| Person 2 | 12-25 hours | 192-400 hours |
| **Total** | **24-50 hours** | **384-800 hours** |

*Note: Flexible schedule accommodating personal commitments, slightly higher due to comparative implementation*

---

## 8. Learning & Portfolio Outcomes

### 8.1 Technical Portfolio Pieces

#### Demonstrable Skills:
- **AI/ML:** Graph RAG implementation, vector databases, LLM integration
- **Technical Architecture:** Framework evaluation and selective adoption
- **Engineering Judgment:** Custom vs. framework trade-off analysis
- **Backend:** API development, database design, data processing
- **Frontend:** Modern React development, AI interface design
- **Full-Stack:** Complete application development and deployment
- **Documentation:** Technical writing and comparative analysis

#### Portfolio Artifacts:
- Live demo website with comparative features
- GitHub repository with both custom and framework implementations
- Technical blog post explaining architecture decisions
- Comparative analysis documentation
- Performance benchmarking results
- Decision framework and recommendations

### 8.2 Learning Documentation

#### Personal Learning Log:
- Custom implementation challenges and solutions
- Framework evaluation criteria and results
- Architecture decisions and trade-offs
- Performance comparison analysis
- Development velocity differences
- Lessons learned about when to build vs. buy
- Recommendations for future similar projects

#### Knowledge Gained:
- Deep practical experience with knowledge graphs
- Understanding of vector similarity search (custom and framework)
- LLM prompt engineering skills (both approaches)
- Full-stack AI application development
- Framework evaluation methodology
- Technical decision-making processes
- Real-world data processing challenges (compared approaches)

---

## 9. Success Metrics - Personal Project

### 9.1 Technical Achievement Metrics

| Goal | Success Criteria | Portfolio Value |
|------|-----------------|-----------------|
| Custom Graph RAG Implementation | System successfully retrieves relevant code sections | High - demonstrates AI/ML fundamentals |
| Framework Evaluation | Documented comparison of approaches | High for architecture roles |
| Technical Decision Making | Clear rationale for tool choices | Very High for senior roles |
| Hybrid Implementation | Optimal blend demonstrating judgment | Very High - shows engineering maturity |

### 9.2 Learning Metrics

| Learning Goal | Measurement | Value |
|---------------|-------------|-------|
| Graph RAG Implementation | Custom system working end-to-end | High |
| Framework Evaluation | Documented comparison of approaches | High for architecture roles |
| Technical Decision Making | Clear rationale for tool choices | Very High for senior roles |
| Performance Analysis | Benchmarking and optimization documentation | High for performance-focused roles |
| Full-Stack AI Development | Complete application with comparative features | Very High - demonstrates range |

### 9.3 Portfolio Impact Metrics

| Metric | Target | Purpose |
|--------|--------|---------|
| GitHub Stars/Interest | 25+ stars | Community validation of technical approach |
| Technical Blog Views | 750+ views | Thought leadership in technical decision-making |
| Interview Opportunities | 3+ interviews mentioning comparative approach | Career advancement |
| Networking Value | 8+ professional connections discussing architecture | Career development |

---

## 10. Project Management - Personal Approach

### 10.1 Lightweight Process

#### Communication:
- Weekly check-ins focusing on comparative findings
- Shared GitHub repository with separate branches for approaches
- Simple task tracking with comparative analysis tasks
- Flexible deadlines based on personal schedules and learning velocity

#### Documentation:
- README-driven development for both implementations
- Comparative analysis documentation template
- Decision log for architecture choices with rationale
- Progress tracking with learning milestone focus

### 10.2 Risk Management

#### Personal Project Risks:
- **Scope Creep:** Keep focused on comparison rather than feature expansion
- **Analysis Paralysis:** Balance evaluation depth with development progress
- **Time Management:** Balance comparative work with other commitments
- **Technical Complexity:** Manage complexity of maintaining parallel implementations

#### Mitigation Strategies:
- Start simple, add comparative complexity gradually
- Set clear evaluation criteria upfront
- Focus on learning and judgment demonstration over perfection
- Document decisions even when pivoting
- Celebrate comparative insights and progress

---

## 11. Open Source & Sharing Strategy

### 11.1 Open Source Approach
- **License:** MIT or Apache 2.0 (permissive)
- **Documentation:** Comprehensive setup guides for both approaches
- **Community:** Welcome feedback on technical decisions
- **Educational Focus:** Emphasize learning value and decision-making process
- **Comparative Value:** Share insights about custom vs. framework trade-offs

### 11.2 Sharing & Networking
- **Technical Blog:** Write detailed post about implementation comparison and decisions
- **Social Media:** Share progress and technical insights
- **Developer Communities:** Present comparative analysis at meetups or online forums
- **Professional Network:** Use as conversation starter about architecture and technical judgment

### 11.3 Future Possibilities
- **Open Source Community:** Framework comparison insights valuable to community
- **Technical Leadership:** Demonstrate decision-making skills for senior roles
- **Consulting Opportunities:** Architecture and tool selection expertise
- **Further Learning:** Apply decision framework to other technical choices

---

## Document Control

**Created:** May 30, 2025  
**Last Modified:** May 30, 2025  
**Next Review:** June 30, 2025  
**Project Status:** Active Development  

---

*This updated PRD reflects the hybrid approach emphasizing both foundational learning through custom implementation and practical engineering judgment through framework evaluation. The comparative approach adds significant portfolio value by demonstrating technical decision-making skills highly valued in senior engineering roles.*
