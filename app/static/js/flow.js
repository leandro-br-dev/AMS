class FlowManager {
    constructor(baseUrl) {
        this.baseUrl = baseUrl;
    }

    async fetchFlows() {
        try {
            const response = await fetch(`${this.baseUrl}/api/flows`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching flows:', error);
        }
    }

    async getFlow(flowId) {
        try {
            const response = await fetch(`${this.baseUrl}/api/flows/${flowId}`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching flow:', error);
        }
    }

    async createFlow(flowData) {
        try {
            const response = await fetch(`${this.baseUrl}/api/flows`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(flowData)
            });
            return await response.json();
        } catch (error) {
            console.error('Error creating flow:', error);
        }
    }

    async updateFlow(flowId, flowData) {
        try {
            const response = await fetch(`${this.baseUrl}/api/flows/${flowId}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(flowData)
            });
            return await response.json();
        } catch (error) {
            console.error('Error updating flow:', error);
        }
    }

    async deleteFlow(flowId) {
        try {
            const response = await fetch(`${this.baseUrl}/api/flows/${flowId}`, {
                method: 'DELETE'
            });
            return await response.json();
        } catch (error) {
            console.error('Error deleting flow:', error);
        }
    }
}

export default FlowManager;
