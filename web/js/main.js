
// GET_DATA FROM TABLE
// const getData = function (){
//                 let data = {
//                 title: title,
//                 list: []
//             }
//
//             const tbody = document.getElementsByTagName('tbody')[0]
//             const tr = tbody.children;
//             for(let i = 0; i < tr.length; i++){
//                 const days = [];
//                 const td = tr[i].children;
//                 for(let j = 1; j < td.length; j++){
//                     if(i !== 0 && i !== tr.length && td[j].children[0].checked){
//                         days.push(td[j].children[0].getAttribute('data-number'))
//                     }
//                 }
//                 try {
//                     if (i !== 0){
//                         data['list'].push({
//                             "full_name": tr[i].children[0].children[0].value,
//                             "days": days
//                         })
//                     }
//                 }
//                 catch (e){
//                     console.log(e)
//                 }
//             }
//             return data;
//             }