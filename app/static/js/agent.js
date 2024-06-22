class AgentManager {
    constructor(baseUrl) {
        this.baseUrl = baseUrl;
    }

    async fetchAgents() {
        try {
            const response = await fetch(`${this.baseUrl}/api/agents`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching agents:', error);
        }
    }

    async getAgent(agentId) {
        try {
            const response = await fetch(`${this.baseUrl}/api/agents/${agentId}`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching agent:', error);
        }
    }

    async createAgent(agentData) {
        try {
            const response = await fetch(`${this.baseUrl}/api/agents`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(agentData)
            });
            return await response.json();
        } catch (error) {
            console.error('Error creating agent:', error);
        }
    }

    async updateAgent(agentId, agentData) {
        try {
            const response = await fetch(`${this.baseUrl}/api/agents/${agentId}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(agentData)
            });
            return await response.json();
        } catch (error) {
            console.error('Error updating agent:', error);
        }
    }

    async deleteAgent(agentId) {
        try {
            const response = await fetch(`${this.baseUrl}/api/agents/${agentId}`, {
                method: 'DELETE'
            });
            return await response.json();
        } catch (error) {
            console.error('Error deleting agent:', error);
        }
    }
}

// Exporting AgentManager for use in other scripts
export default AgentManager;
