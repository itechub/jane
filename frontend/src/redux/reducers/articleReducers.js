import TYPES from "redux/types/articleTypes";

const initialState = {
  user: {},
  tags: [],
  article: {},
  articleList: [],
  compose: {
    articleId: null,
    title: "",
    editorState: "",
    selectedTags: []
  }
};
const articles = (state = initialState, action) => {
  switch (action.type) {
    case TYPES.RECEIVE_USER:
      return Object.assign({}, state, {
        user: action.user
      });
    case TYPES.UPDATE_ARTICLE_EDITOR:
      return {
        ...state,
        compose: {
          ...state.compose,
          ...action.data
        }
      };
    case TYPES.GET_TAG_LIST:
      return Object.assign({}, state, {
        tags: action.tags
      });
    case TYPES.RECEIVE_ARTICLE_INSTANCE:
      return Object.assign({}, state, {
        article: action.article
      });
    case TYPES.RECEIVE_ARTICLE_LIST:
      return Object.assign({}, state, {
        articleList: action.articles
      });
    default:
      return state;
  }
};

export default articles;
