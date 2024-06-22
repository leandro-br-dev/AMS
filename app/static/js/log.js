class LogManager {
    constructor(baseUrl) {
        this.baseUrl = baseUrl;
    }

    async fetchLogs() {
        try {
            const response = await fetch(`${this.baseUrl}/api/logs`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching logs:', error);
        }
    }

    async getLog(logId) {
        try {
            const response = await fetch(`${this.baseUrl}/api/logs/${logId}`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching log:', error);
        }
    }

    async createLog(logData) {
        try {
            const response = await fetch(`${this.baseUrl}/api/logs`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(logData)
            });
            return await response.json();
        } catch (error) {
            console.error('Error creating log:', error);
        }
    }

    async updateLog(logId, logData) {
        try {
            const response = await fetch(`${this.baseUrl}/api/logs/${logId}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(logData)
            });
            return await response.json();
        } catch (error) {
            console.error('Error updating log:', error);
        }
    }

    async deleteLog(logId) {
        try {
            const response = await fetch(`${this.baseUrl}/api/logs/${logId}`, {
                method: 'DELETE'
            });
            return await response.json();
        } catch (error) {
            console.error('Error deleting log:', error);
        }
    }
}

export default LogManager;
