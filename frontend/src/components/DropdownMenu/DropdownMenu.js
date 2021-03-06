import React, { Fragment } from "react";
import { withRouter } from "react-router";
import { connect } from "react-redux";
import { Avatar, Menu } from "antd";
import { Link } from "react-router-dom";

const { SubMenu } = Menu;

const DropdownMenu = props => {
  if (props.isAuthenticated) {
    return (
      <Menu
        key="user"
        mode="horizontal"
        onClick={() => {}}
        style={{ lineHeight: "63px" }}
        className="user-section"
      >
        <SubMenu
          title={
            <Fragment>
              <span style={{ color: "#999", marginRight: 4 }}>Hi,</span>
              <span>{props.user.username}</span>
              <Avatar style={{ marginLeft: 8 }} src={props.avatar} />
            </Fragment>
          }
        >
          <Menu.Item key="profile">
            <Link to={`/${props.user.username}`} key="profile">
              Profile
            </Link>
          </Menu.Item>
          <Menu.Item key="SignOut" onClick={props.onLogout}>
            Logout
          </Menu.Item>
        </SubMenu>
      </Menu>
    );
  }
  return (
    <Link to="/login" key="login">
      Login in
    </Link>
  );
};

const mapStateToProps = state => {
  const { user, isAuthenticated } = state.authentication;
  return { user, isAuthenticated };
};

export default withRouter(connect(mapStateToProps)(DropdownMenu));
