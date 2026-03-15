**Agentic AI Frameworks**


**Why we need frameworks for building agentic systems**

Frameworks are essential and plays a vital role in the AI agent development. With out frameworks, we need handle our self all alone the following 
1. Prompt design
2. External tool calling, configurations and management
3. Decisions
4. LLM configurations
5. Monitoring

There are two broad categories of Agentic AI frameworks
1. Coding frameworks

   **Lang chain:** 
   - This is an open source framework
   - Useful to pick when building the simple work flows
   - Relatively simple to understand, hence faster to implement
   - Can be managed to configure multiple LLM's
   
   **Lang graph**
   - Build on top of Lang chain to support complex work flows
   - Multi agents can be managed to build with Lang graph
   - Supports human in loop
   - Supports multi step work flows
   - Take autonomous actions
   - Can run some tasks for longer time
   - Can schedule a task
   
   **Crew AI**
   - Multi agent applications can be build
   - used to build applications where multiple agents need to work together as a team
   - Examples: reasearch agent, image generation agent, review agent etc
   
   **Google ADK (Agent Development Kit)**
   - Named as model agnostic framework meaning any model can be easily and smoothly integrated
   - Best fit for organisations with in Google eco systems
   - Works best with Google Gemini LLM
   
   **Autogen**
   - Best fit for organisations with in Microsoft eco system
   
   **Vercel AI SDK**
   - Best for web applications 
   - Type script tool for building AI agentic applications
   
2. Non-coding frameworks
    Example: N8N
    Purpose: Follows Low code or no code principle
    - use this when there are no coding expertise is available
    - useful when automating the business workflows and approval works flow automation is essential
    - Strongly recommended when human in loop for the feedback are required
     
    
In Summary,
- Use _Lang chain_ for simple workflow applications
- For complex workflows with multi agentic scenarios and need more control over task executions -> any coding framework except Langchain
- With in GCP eco system - use Google ADK
- With in Microsoft eco system - use Autogen
- For web applications/type scripting - use Vercel AI 
- For automating the workflows - use N8N 