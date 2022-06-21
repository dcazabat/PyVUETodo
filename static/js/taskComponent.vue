export default {
    data() {
        return {
          task: {
            title: '',
          },
          tasks: [],
        }
      },
      async created(){
        await this.getTasks()
      },
      methods: {
        async sendRequest(url, method, data){
          const my_headers = new Headers({
            'Content-type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
          })
          // console.log(url, my_headers, data)
          const reponse = await fetch(url, {
            method: method,
            headers: my_headers,
            body: data,
          })
          return reponse
        },
        async getTasks() {
            const reponse = await this.sendRequest(window.location, 'get')
            this.tasks = await reponse.json()
        },
        async addTask() {
            await this.getTasks()
    
            await this.sendRequest(window.location + 'add', 'post', JSON.stringify(this.task))
    
            await this.getTasks()
    
            this.task.title = ''
        },
        async deleteTask(task) {
          await this.sendRequest(window.location + 'delete','post', JSON.stringify(task))
    
          await this.getTasks()
        },
        async completeTask(task) {
          await this.sendRequest(window.location + 'complete','post', JSON.stringify(task))
    
          await this.getTasks()
        },
      },
      delimiters: ['{', '}']
    }