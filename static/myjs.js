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


window.onload = function(){
const test=document.getElementById('testowo');
test.innerHTML='dupowaty test';}



function removeElementsByClass(className){
    const elements = document.getElementsByClassName(className);
    while(elements.length > 0){
        elements[0].parentNode.removeChild(elements[0]);
    }
}

const dodanyId=0
//////////////////////////////Tutaj wrzucę ajaxa który będzie dynamicznie aktualizował tabelę//////////////
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
            div.innerHTML+=item.fields.skladnik
            div.innerHTML+='<br>'
            console.log('div',div);
            tabelaDocelowa.appendChild(div);})
            },
            error : function (error){console.log('error')},
            })
/////////////////////////////a tutaj koniec ajaxa, który aktualizuję tabelę/////////////






skladnikBox.addEventListener( 'change', e=>{console.log( event.target.value );

                                        skl=event.target.selectedOptions[0].text;
                                        console.log(skl);
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
                                        }
                                        })
                                        /////tu wstawiam///
                                        dodajSkladnikButton.addEventListener('click',e=>{console.log('kliknąłem');
                                            ///tworzenie daty formulara i odpowiedzi do ajaxa////////////////////
                                            dataf={'csrfmiddlewaretoken': csrf[0].value,'skladnik':skl}
                                            console.log('elementyForm',elementyForm)
                                            console.log('idwdataf',`${skl}-${i}`)
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
                                                      const listaskladnikow=response.tabela
                                                      for (const [key, value] of Object.entries(listaskladnikow)) {
                                                          const div=document.createElement('div')

                                                          div.innerHTML+=key
                                                          div.innerHTML+=value
                                                          prowizorycznatabelaBox.appendChild(div)
                                                        }

                                                      const div=document.createElement('div')
                                                      div.innerHTML+=listaskladnikow.skladnik
                                                      console.log('listaskladnikow.skladnik',listaskladnikow.skladnik)
                                                      tabelaDocelowa.appendChild(div)


                                                      removeElementsByClass('elFormDelete');
                                                      $("#exampleModal").modal('hide');


                                                                    },
                                           error : function(error){
                                                        console.log(' dupa nie działa');



//
                                                                                }
                                     });
                                     /////koniec ajaxa

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


















