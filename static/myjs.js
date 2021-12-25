console.log('O co tu chodzi?')
console.log('dupa?')
const modalBox=document.getElementById("exampleModal")
const skladnikBox= document.getElementById('wybieraj');
const modalTytul=document.getElementById("exampleModalLabel")
const formBox= document.getElementById('modal-form')
const closeButton=document.getElementById('close-button')
const dodajSkladnikButton=document.getElementById("dodajsklbutton")
const prowizorycznatabelaBox=document.getElementById('prowizorycznatabela')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const tabelaDocelowa=document.getElementById('tabela-docelowa')
//console.log('tabelaDocelowa',tabelaDocelowa)
const deleteButtons=document.getElementsByClassName("btn-close")

console.log('close buttons', deleteButtons)
window.onload = function(){
const test=document.getElementById('testowo');
test.innerHTML='dupowaty test';}

////////funkcja z ajaxem do aktualizacji taveli///////
function updateTable(){
         $.ajax({
            type: 'GET',
            url: 'aktualizujTabela/',
            success : function(response){
            console.log('Sukces ajaxa z tabelą', response);
            let elementyTabeli=response.tabela_zbiorcza
            console.log('elementyTabeli', response.tabela_zbiorcza)

            //let tabelaDocelowa=document.getElementById("tabela-docelowa");

            elementyTabeli.map(item=>{
            console.log('itemTabeli',item.fields.skladnik);
            const div=document.createElement('div')
            ///////dodawanie przycisku do usuwania////////////////
            var deleteButton = document.createElement("button");

//          element.type = type;type="button" class="close" data-dismiss="modal" aria-label="Close"
            deleteButton.setAttribute('type','button');
            deleteButton.setAttribute('class',"btn-close");
            deleteButton.setAttribute('aria-label','Close');
            deleteButton.setAttribute('id',item.pk);
            deleteButton.setAttribute('onclick',delItem);
            deleteButton.onclick = function() {
            $.ajax({
                type: 'GET',
                url: `delSkl/${ item.pk }/`,
                success : function(response){console.log('sukces ajaxa z del');

                },//koniec sukcesa
                error : function (error){console.log('brak sukcesu ajaxa z del')},
                })


            //alert("blabla");
          };
            //////////////////////////////////////////////////////
            div.innerHTML+=item.fields.skladnik+'  '+item.fields.gramy
            console.log('div',div);
            div.appendChild(deleteButton);
            tabelaDocelowa.appendChild(div);
            //div.innerHTML+='<br>'


            })
            },
            error : function (error){console.log('error')},
            })
}
//////////koniec funkcji z ajaxem do aktualizacji tabeli//////

function removeElementsByClass(className){
    const elements = document.getElementsByClassName(className);
    while(elements.length > 0){
        elements[0].parentNode.removeChild(elements[0]);
    }
}

const dodanyId=0

updateTable()
//////////////////////////////Tutaj wrzucę ajaxa który będzie dynamicznie aktualizował tabelę//////////////
// $.ajax({
//            type: 'GET',
//            url: 'aktualizujTabela/',
//            success : function(response){
//            console.log('Sukces ajaxa z tabelą', response);
//            let elementyTabeli=response.tabela_zbiorcza
//            console.log('elementyTabeli', response.tabela_zbiorcza)
//
//            //let tabelaDocelowa=document.getElementById("tabela-docelowa");
//
//            elementyTabeli.map(item=>{
//            console.log('itemTabeli',item.fields.skladnik);
//            const div=document.createElement('div')
//            ///////dodawanie przycisku do usuwania////////////////
//            var deleteButton = document.createElement("button");
//
////          element.type = type;type="button" class="close" data-dismiss="modal" aria-label="Close"
//            deleteButton.setAttribute('type','button');
//            deleteButton.setAttribute('class',"btn-close");
//            deleteButton.setAttribute('aria-label','Close');
//            deleteButton.setAttribute('id',item.pk);
//            deleteButton.setAttribute('onclick',delItem);
//            deleteButton.onclick = function() {
//            $.ajax({
//                type: 'GET',
//                url: `delSkl/${ item.pk }/`,
//                success : function(response){console.log('sukces ajaxa z del');
//
//                },//koniec sukcesa
//                error : function (error){console.log('brak sukcesu ajaxa z del')},
//                })
//
//
//            //alert("blabla");
//          };
//            //////////////////////////////////////////////////////
//            div.innerHTML+=item.fields.skladnik+'  '+item.fields.gramy
//            console.log('div',div);
//            div.appendChild(deleteButton);
//            tabelaDocelowa.appendChild(div);
//            //div.innerHTML+='<br>'
//
//
//            })
//            },
//            error : function (error){console.log('error')},
//            })
/////////////////////////////a tutaj koniec ajaxa, który aktualizuję tabelę/////////////

function delItem() {
  alert("blabla");
}




skladnikBox.addEventListener( 'change', e=>{console.log( 'event.target.value',event.target.value );

                                        skl=event.target.selectedOptions[0].text;
                                        console.log('skl',skl);
                                       modalTytul.innerText=event.target.selectedOptions[0].text;
``
                                       $("#exampleModal").modal('show');
                                       ////////////////ajax pobieranie elementów formularza///////////////////////////////

                                       $.ajax({
                                        type: 'GET',
                                        url: `formJson/${ skl }/`,
                                        success : function(response){
                                        console.log('succes spobrania do forma', response);
                                        let elementyForm = response.datadict

                                        elementyForm.map(item=>{
                                        if(Array.isArray(item)){if (item[0]==='producent'){
                                            console.log('mamy tabelę');
                                            const label=document.createElement('label')
                                            label.textContent=item[0]
                                            label.setAttribute('class','elFormDelete');
                                            const select=document.createElement('select');
                                            select.setAttribute('class',"ui dropdown");
                                            //select.setAttribute('id',"optionId");
                                            select.setAttribute('class','elFormDelete')
                                            select.setAttribute('id',`${skl}-${item[0]}`)
                                            console.log('idwimpucie',`${skl}-${item[0]}`)
                                            formBox.appendChild(label)
                                            formBox.appendChild(select)
                                            //const optionBox= document.getElementById('optionId')
                                            const optionBox= document.getElementById(`${skl}-${item[0]}`)
                                            const slicedArray=item.slice(1)
                                            console.log(item[0])
                                            slicedArray.map(elem=>{
                                            const option=document.createElement('option')
                                            option.textContent = elem
                                            optionBox.appendChild(option)
                                            })}else{ console.log('tutaj będzie select z imputem');
                                            {
                                            console.log('mamy tabelę');
                                            const label=document.createElement('label');
                                            label.textContent=item[0]
                                            label.setAttribute('class','elFormDelete');
                                            const br=document.createElement('br')
                                            br.setAttribute('class','elFormDelete')
                                            const select=document.createElement('select');
                                            select.setAttribute('class',"ui dropdown");
                                            //select.setAttribute('id',"optionId");
                                            select.setAttribute('class','elFormDelete')
                                            select.setAttribute('id',`${skl}-${item[0]}`)
                                            console.log('idwimpucie',`${skl}-${item[0]}`)
                                            formBox.appendChild(label)
                                            formBox.appendChild(select)
                                            formBox.appendChild(br)
                                            //const optionBox= document.getElementById('optionId')
                                            const optionBox= document.getElementById(`${skl}-${item[0]}`)
                                            const slicedArray=item.slice(1)
                                            console.log(item[0])
                                            slicedArray.map(elem=>{
                                            const option=document.createElement('option')
                                            option.textContent = elem
                                            optionBox.appendChild(option)
                                            })}
                                            }
                                        }else{


                                        if (item=='aa'){
                                        const label=document.createElement('label')
                                        label.textContent=item
                                        const check = document.createElement("input");
                                        check.setAttribute('type',"checkbox")
                                        check.setAttribute('value','off')
                                        check.setAttribute('id',`${skl}-${item}`)
                                        console.log('idwimpucie',`${skl}-${item}`)
                                        check.setAttribute('class','elFormDelete')
                                        label.setAttribute('class','elFormDelete')
                                        //check.setAttribute('class','checkBox')
                                        check.setAttribute('name','checkBox')
                                        formBox.appendChild(check)
                                        formBox.appendChild(label)
                                        console.log('checkvalue',check.value)
                                        } else
                                        {
                                        const label=document.createElement('label')
                                        const input=document.createElement('input')
                                        input.setAttribute('class','elFormDelete')
                                        label.setAttribute('class','elFormDelete')
                                        input.setAttribute('id',`${skl}-${item}`)
                                        console.log('idwimpucie',`${skl}-${item}`)
                                        const br=document.createElement('br')
                                        br.setAttribute('class','elFormDelete')
                                        label.textContent=item
                                        formBox.appendChild(label)
                                        formBox.appendChild(input)
                                        formBox.appendChild(br)
                                        }}
                                        })


                                        dodajSkladnikButton.addEventListener('click',e=>{console.log('kliknąłem');
                                            /////tutaj wstawię kod który będzie sprawdzał czy radio button jest wciśnięty///
                                            const checkButtons = document.getElementsByName('checkBox')
                                            console.log('checkButtons',checkButtons)
                                            for (let check of checkButtons){if (check.checked){ check.value='on'}else{check.value='off'}}
                                            /////////////////////////////////////////////////////////////////////////////
                                            ///tworzenie daty formulara i odpowiedzi do ajaxa////////////////////
                                            dataf={'csrfmiddlewaretoken': csrf[0].value,'skladnik':skl}
                                            console.log('elementyForm',elementyForm)
                                            //console.log('idwdataf',`${skl}-${i}`)
                                            for ( var i in elementyForm )if ( Array.isArray(elementyForm[i])){ console.log('na razie nie umiem tabeli',`${skl}-${elementyForm[i][0]}`);dataf[elementyForm[i][0]]=document.getElementById(`${skl}-${elementyForm[i][0]}`).value}else{console.log('i',i,`${skl}-${elementyForm[i]}`);dataf[elementyForm[i]]=document.getElementById(`${skl}-${elementyForm[i]}`).value}
                                            console.log('elementyForm',elementyForm)
                                            console.log('dataf',dataf)
                                          $.ajax({
                                           type: 'POST' ,
                                           url:'/dodajskl/',
                                           data : dataf,
                                           success: function(response){
                                                      console.log('wygrywamy');
                                                      console.log('response.tabela',response.tabela)

//                                                      wypisywanie skladników
//                                                      const listaskladnikow=response.tabela
//                                                      for (const [key, value] of Object.entries(listaskladnikow)) {
//                                                          const div=document.createElement('div')
//
//                                                          div.innerHTML+=key
//                                                          div.innerHTML+=value
//                                                          prowizorycznatabelaBox.appendChild(div)
//                                                        }

//                                                      const div=document.createElement('div')
//                                                      div.innerHTML+=listaskladnikow.skladnik +'  '+listaskladnikow.gramy
//                                                      console.log('listaskladnikow.skladnik',listaskladnikow.skladnik)
//                                                      tabelaDocelowa.appendChild(div)
                                                        tabelaDocelowa.innerHTML=''
                                                        updateTable()
                                                                    },
                                           error : function(error){
                                                        console.log(' dupa nie działa');

                                                                                }
                                     });
                                     /////koniec ajaxa
                                     removeElementsByClass('elFormDelete');
                                                      $("#exampleModal").modal('hide');

                                     })

                                        /////tu koniec wstawania//////

                                        },
                                        error : function (response){
                                        console.log('error', error)}
                                        }),
                                        skladnikBox.selectedIndex = 0;

                                     })

//////////////////////3pozycja/////////////////////////////////////////////////////

closeButton.addEventListener('click',e=>{console.log('kliknąłem close ');$("#exampleModal").modal('hide');
                                           removeElementsByClass('elFormDelete'); })

















