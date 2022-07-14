import React, { Component } from 'react'
import {Animated} from "react-animated-css";
import './Home.css';
import {AiFillEdit} from 'react-icons/ai'
import "bootstrap/dist/css/bootstrap.min.css";
import { Container } from 'react-bootstrap';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import Dropdown from 'react-bootstrap/Dropdown';
import vacancy from './images/vacancy.png'
import company from './images/company.png'
import newjob from './images/newjob.png'

import Select, { StylesConfig }  from 'react-select'

import {HiLocationMarker} from "react-icons/hi";
import {HiSortAscending} from "react-icons/hi";
import {HiSortDescending} from "react-icons/hi";
import {FaRegClock} from 'react-icons/fa';
import {FaRegMoneyBillAlt} from 'react-icons/fa';
import {FaRegCalendarAlt} from 'react-icons/fa';

import Navb from "./Navb";
import Foot from "./Foot";

const options = [
    { value: 'devops', label: 'devops' },
    { value: 'react', label: 'react' },
    { value: 'software engineer', label: 'software engineer' }
  ]
const CatOptions = [
    { value: 'teacher', label: 'teacher' },
    { value: 'developer', label: 'developer' },
    { value: 'software engineer', label: 'software engineer' }
  ]
const TitleOptions = [
    { value: 'Govt', label: 'Govt' },
    { value: 'Non-Govt', label: 'Non-Govt' },
    { value: 'NGO', label: 'NGO' }
  ]
  const OrgOptions = [
    { value: 'Govt', label: 'Govt' },
    { value: 'Non-Govt', label: 'Non-Govt' },
    { value: 'NGO', label: 'NGO' }
  ]
  const LocationOptions = [
    { value: 'Dhaka', label: 'Dhaka' },
    { value: 'Rajshahi', label: 'Rajshahi' },
    { value: 'Rangpur', label: 'Rangpur' },
    { value: 'Sylhet', label: 'Sylhet' },
    { value: 'Khulna', label: 'Khulna' },
    { value: 'Chittagoan', label: 'Chittagoan' }
  ]

export class Home extends Component {
  render() {
    return (
       <React.Fragment>
       <body>
       <Navb/>
       <div className='homebg'>
            <div className='container-fluid mb-5 wow fadeIn'></div>
            <div className='floatingdiv'> 
                <div className='row g-2'>
                    <div className='col-md-12'>
                        <Select options={options} openMenuOnFocus isClearable  placeholder='Keyword' />
                    </div>
                    <div className='col-md-2'>
                        <Select options={CatOptions} openMenuOnFocus isClearable  placeholder='Category' />
                    </div>
                    <div className='col-md-3'>
                        <Select closeMenuOnSelect={false}
                                isMulti
                                options={TitleOptions} openMenuOnFocus isClearable placeholder='Title' />
                    </div>
                    <div className='col-md-3'>
                        <Select options={OrgOptions} openMenuOnFocus isClearable  placeholder='Organization' />
                    </div>
                    <div className='col-md-2'>
                        <Select options={LocationOptions} openMenuOnFocus isClearable  placeholder='Location' />
                    </div>
                    <div className='col-md-2'>
                        <button className='btn btn-success'>Search</button>
                    </div>
                </div>
            </div>
            <div className='nicherdiv mb-3'> 
                <div className=' vacancydiv' >
                    <img className='vacancy' src={vacancy}></img>
                    
                </div> 
                
                <div className='companydiv'>
                     <img className='company' src={company}></img>

                </div>
                <div className='newjobdiv'>
                    <img className='newjob' src={newjob}></img>
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
       {/* <Foot margin_value={172}/> */}
       </body>
       </React.Fragment>
    )
  }
}

export default Home