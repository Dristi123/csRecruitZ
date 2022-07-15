
import React, {Component, useState} from 'react'


import {Animated} from "react-animated-css";
import './Home.css';
import "bootstrap/dist/css/bootstrap.min.css";
import Form from 'react-bootstrap/Form';
import vacancy from './images/vacancy.png'
import company from './images/company.png'
import newjob from './images/newjob.png'

import Select, { StylesConfig }  from 'react-select'

import {HiLocationMarker} from "react-icons/hi";
import {FaRegClock} from 'react-icons/fa';
import {FaRegMoneyBillAlt} from 'react-icons/fa';
import {FaRegCalendarAlt} from 'react-icons/fa';

import Navb from "./Navb";
import Foot from "./Foot";
import {Navigate} from "react-router-dom";


const options = [
    { value: 'devops', label: 'devops' },
    { value: 'react', label: 'react' },
    { value: 'software engineer', label: 'software engineer' }
  ]
const CatOptions = [
    { value: 'Teaching', label: 'Teaching' },
    { value: 'DevOps', label: 'DevOps' },
    { value: 'Security', label: 'Security' },
    { value: 'Research and Development', label: 'Research and Development' },
    { value: 'Programming', label: 'Programming' },
  ]
const NatureOptions = [
    { value: 'Part-time', label: 'Part-time' },
    { value: 'Full-time', label: 'Full-time' },
    { value: 'Remote', label: 'Remote' },
    { value: 'Freelancing', label: 'Freelancing' }
  ]
  const OrgOptions = [
    { value: 'Government', label: 'Government' },
    { value: 'Semi Government', label: 'Semi Government' },
    { value: 'NGO', label: 'NGO' },
    { value: 'Private Firm', label: 'Private Firm' },
    { value: 'International Agencies', label: 'International Agencies' }
  ]
  const LocationOptions = [
    { value: 'Dhaka', label: 'Dhaka' },
    { value: 'Rajshahi', label: 'Rajshahi' },
    { value: 'Rangpur', label: 'Rangpur' },
    { value: 'Sylhet', label: 'Sylhet' },
    { value: 'Khulna', label: 'Khulna' },
    { value: 'Chittagong', label: 'Chittagong' },
    { value: 'Mymensingh ', label: 'Mymensingh ' },
    { value: 'Barishal', label: 'Barishal' }
  ]

var jsonData = {
    "category":"",
    "organization":"",
    "location":"",
    "keyword":"",
    "nature":""
  }





export class Home extends Component {

    state={
        cat: { value: 'Category', label: 'Category' },
        keyword:"keyword",
        org :{ value:'Organization',label:'Organization'},
        loc :{ value:'Location',label:'Location'},
        nature:{ value:'Job Nature',label:'Job Nature'},
        redirect:false

    };
    constructor(props) {
    super(props);
    this.handleClick=this.handleClick.bind(this);
  }


  handler = (event) => {
      const value = event.value
      console.log(value)
      this.state.cat.value=value
      this.state.cat.label=value
      jsonData.category=value
    }
     handlerorg = (event) => {
      const value = event.value
      console.log(value)
      this.state.org.value=value
      this.state.org.label=value
      jsonData.organization=value
    }
     handlerloc = (event) => {
      const value = event.value
      console.log(value)
      this.state.loc.value=value
      this.state.loc.label=value
      jsonData.location=value
    }
    handlernature = (event) => {
      const value = event.value
      console.log(value)
      this.state.nature.value=value
      this.state.nature.label=value
      jsonData.nature=value
    }
    handlerkeyword= (event) => {
      const value = event.target.value
      console.log(value)
      this.state.keyword=value

      jsonData.keyword=value
    }

handleClick() {
    //const history = useNavigate();
    // Send data to the backend via POST

    fetch('http://127.0.0.1:8000/searchinput/', {  // Enter your IP address here

      method: 'POST',
        headers:{
        'Content-Type': 'application/json',
      },
      mode: 'cors',
      body: JSON.stringify(jsonData) // body data type must match "Content-Type" header
    })
    this.setState({'redirect':true})

  }
    // constructor(props) {
    //     super(props);
    //   }
  render() {

        //const { navigation } = this.props;
        //this.setState({navigation})
    // const TagsInput = props => {
    //     const [tags, setTags] = React.useState(props.tags);
    //     const removeTags = indexToRemove => {
    //         setTags([...tags.filter((_, index) => index !== indexToRemove)]);
    //     }
    // };
    // const addTags = event => {
    //     if (event.target.value !== "") {
    //         setTags([...tags, event.target.value]);
    //         props.selectedTags([...tags, event.target.value]);
    //         event.target.value = "";
    //     }
    // };
    return (
       <React.Fragment>
       <body>
       <Navb/>
       <div className='homebg'>
            <div className='container-fluid mb-5 wow fadeIn'></div>
            <div className='floatingdiv'> 
                <div className='row g-2'>
                    <div className='col-md-12'>
                    {/* <TextField
                        // value={value}
                        // onChange={(e) => {
                        //     setValue(e.target.value);
                        // }}
                        /> */}
                        <Form >
                            <input style={{width:'1202px', padding:'7px'}} type="text"  onChange={this.handlerkeyword} placeholder='Keyword'></input>
                        </Form>
                        {/* <div className="tags-input">
                            <ul id="tags">
                                {tags.map((tag, index) => (
                                    <li key={index} className="tag">
                                        <span className='tag-title'>{tag}</span>
                                        <span className='tag-close-icon'
                                            onClick={() => removeTags(index)}
                                        >
                                            x
                                        </span>
                                    </li>
                                ))}
                            </ul>
                            <input
                                type="text"
                                onKeyUp={event => event.key === "Enter" ? addTags(event) : null}
                                placeholder="Press enter to add tags"
                            />
                        </div> */}
                    </div>


                    <div className='col-md-3'>
                        <Select options={CatOptions} value={this.state.cat}  onChange={this.handler} isClearable placeholder="Category" />
                    </div>


                    <div className='col-md-3'>
                        <Select 

                                options={NatureOptions} value={this.state.nature}  onChange={this.handlernature} openMenuOnFocus isClearable placeholder='Job Nature' />
                    </div>
                    <div className='col-md-3'>
                        <Select options={OrgOptions} value={this.state.org}  onChange={this.handlerorg}openMenuOnFocus isClearable  placeholder='Organization' />
                    </div>
                    <div className='col-md-2'>
                        <Select options={LocationOptions} value={this.state.loc}  onChange={this.handlerloc} openMenuOnFocus isClearable  placeholder='Location' />
                    </div>


                    <div className='col-md-1'>
                        <button className='btn btn-success' onClick={this.handleClick}>Search</button>

                    </div>




                </div>
            </div>
            <div className='nicherdiv mb-3'> 
                <div className=' vacancydiv' >
                    <a href='//'><img className='vacancy' src={vacancy}></img></a>
                    <h2 className='vacancytitle'>Vacancy</h2>
                </div> 
                
                <div className='companydiv'>
                    <a href='//'> <img className='company' src={company}></img></a>
                    <h2 className='companytitle'>Company</h2>
                </div>
                <div className='newjobdiv'>
                    <a href='//'>
                        <img className='newjob' src={newjob}></img>
                    </a>
                    <h2 className='newjobtitle'>New job</h2>
                </div>
         
                
            </div>

            <Animated animationIn="slideInLeft"  animationInDuration={1800}  isVisible={true}>

            <div className='recommendationdiv mb-3'> 
                <h3 style={{fontWeight:'bold',marginLeft:'2%',padding:'15px',textDecorationLine:'underline'

                }}>Recommendation for you</h3>
                <div className="jobdiv">
                    <h4 style={{color:"#29A335"}}>Software Engineer</h4>
                    <h6 style={{color:"black"}}>Optimizely</h6>

                    <p style={{display:"inline"}}><HiLocationMarker style={{
                        color:"#29A335",
                        paddingRight:5,
                        marginTop:-2
                    }}/>Banani, Dhaka</p>

                    <p className="fulltime_p"><FaRegClock style={{
                        color:"#29A335",
                        paddingRight:5,
                        marginTop:-2
                    }}/>Full-time</p>

                    <p className="salary_p"><FaRegMoneyBillAlt style={{
                        color:"#29A335",
                        paddingRight:5,
                        marginTop:-2
                    }}/>50,000 BDT</p>

                    <p className="float_right_p"><FaRegCalendarAlt style={{
                        color:"#29A335",
                        paddingRight:5,
                        marginTop:-2
                    }}/>Deadline: 31 July, 2022</p>

                    <button className="float_right_btn">View Details</button>
                </div>
                <div className="jobdiv">
                    <h4 style={{color:"#29A335"}}>Software Engineer</h4>
                    <h6 style={{color:"black"}}>Optimizely</h6>

                    <p style={{display:"inline"}}><HiLocationMarker style={{
                        color:"#29A335",
                        paddingRight:5,
                        marginTop:-2
                    }}/>Banani, Dhaka</p>

                    <p className="fulltime_p"><FaRegClock style={{
                        color:"#29A335",
                        paddingRight:5,
                        marginTop:-2
                    }}/>Full-time</p>

                    <p className="salary_p"><FaRegMoneyBillAlt style={{
                        color:"#29A335",
                        paddingRight:5,
                        marginTop:-2
                    }}/>50,000 BDT</p>

                    <p className="float_right_p"><FaRegCalendarAlt style={{
                        color:"#29A335",
                        paddingRight:5,
                        marginTop:-2
                    }}/>Deadline: 31 July, 2022</p>

                    <button className="float_right_btn">View Details</button>
                </div>
                <div className="jobdiv">
                    <h4 style={{color:"#29A335"}}>Software Engineer</h4>
                    <h6 style={{color:"black"}}>Optimizely</h6>

                    <p style={{display:"inline"}}><HiLocationMarker style={{
                        color:"#29A335",
                        paddingRight:5,
                        marginTop:-2
                    }}/>Banani, Dhaka</p>

                    <p className="fulltime_p"><FaRegClock style={{
                        color:"#29A335",
                        paddingRight:5,
                        marginTop:-2
                    }}/>Full-time</p>

                    <p className="salary_p"><FaRegMoneyBillAlt style={{
                        color:"#29A335",
                        paddingRight:5,
                        marginTop:-2
                    }}/>50,000 BDT</p>

                    <p className="float_right_p"><FaRegCalendarAlt style={{
                        color:"#29A335",
                        paddingRight:5,
                        marginTop:-2
                    }}/>Deadline: 31 July, 2022</p>

                    <button className="float_right_btn">View Details</button>
                </div>
            </div>
            </Animated>
             

       </div>
       <Foot margin_value={172}/>
       {this.state.redirect && <Navigate to='/joblist' replace={true}/>}
       </body>
       </React.Fragment>
    )
  }
}

export default Home;
//export default withRouter(Home);

// export default function(props) {
//   const navigation = useNavigate();
//
//   return <Home {...props} navigation={navigation} />;
// }